"""
Unit tests for Relationship Reflection and Legal Information modules.
"""

import pytest
from src.assessment.questionnaire import QuestionnaireManager, QuestionnaireResponse
from src.assessment.relationship_reflection import RelationshipReflectionEngine
from src.assessment.legal_information import LegalInformationGuide


def test_questionnaire_manager_safety_detection():
    mgr = QuestionnaireManager()

    # Normal response without safety issues
    resp_normal = QuestionnaireResponse(
        concerns=["Communication breakdown"],
        discussion_safety="somewhat_tense",
    )
    assert mgr.validate_safety_flags(resp_normal) is False

    # Response with explicit unsafe flag
    resp_unsafe_flag = QuestionnaireResponse(
        discussion_safety="unsafe_or_fearful",
    )
    assert mgr.validate_safety_flags(resp_unsafe_flag) is True

    # Response with domestic violence concern
    resp_dv = QuestionnaireResponse(
        concerns=["Physical safety concerns or domestic violence"],
    )
    assert mgr.validate_safety_flags(resp_dv) is True


def test_relationship_reflection_safety_escalation():
    engine = RelationshipReflectionEngine()

    resp_dv = QuestionnaireResponse(
        concerns=["Physical safety concerns or domestic violence"],
        discussion_safety="unsafe_or_fearful",
    )
    rep = engine.generate_reflection_report(resp_dv)

    assert rep["is_diagnostic"] is False
    assert rep["safety_guidance"] is not None
    assert rep["safety_guidance"]["priority_status"] == "URGENT_SAFETY_PRIORITY"
    # Verify 181 Women Helpline and 112 ERSS are provided
    contacts = [c["contact"] for c in rep["safety_guidance"]["official_support_contacts"]]
    assert "181" in contacts
    assert "112" in contacts


def test_relationship_reflection_non_diagnostic_no_probabilities():
    engine = RelationshipReflectionEngine()

    resp = QuestionnaireResponse(
        concerns=["Communication breakdown", "Financial disagreement / Stress"],
        user_goal="reconciliation_pathways",
    )
    rep = engine.generate_reflection_report(resp)

    assert rep["safety_guidance"] is None
    assert len(rep["reflection_themes"]) == 2
    # Ensure no numerical probability fields or predictive scores are calculated or presented
    assert "probability" not in rep
    assert "divorce_score" not in rep
    assert "prediction" not in rep
    assert "% chance" not in str(rep).lower()


def test_legal_information_guide_statutes():
    guide = LegalInformationGuide()

    hma = guide.get_statutory_details("hindu_marriage_act")
    assert hma["statute_name"] == "Hindu Marriage Act, 1955"
    sections = [s["section"] for s in hma["key_sections"]]
    assert "Section 13(1)" in sections
    assert "Section 13B" in sections
    assert "Section 24" in sections


def test_legal_information_procedural_tracks():
    guide = LegalInformationGuide()

    mutual = guide.get_procedural_track("mutual_consent")
    assert "Mutual Consent" in mutual["name"]
    assert len(mutual["stages"]) == 5

    contested = guide.get_procedural_track("contested")
    assert "Contested" in contested["name"]
    assert len(contested["stages"]) >= 7


def test_legal_information_precedents_and_legal_aid():
    guide = LegalInformationGuide()
    full_guide = guide.get_comprehensive_guide()

    assert "Amardeep Singh v. Harveen Kaur" in str(full_guide["landmark_precedents"])
    assert "Rajnesh v. Neha" in str(full_guide["landmark_precedents"])
    assert "Tamil Nadu State Legal Services Authority" in full_guide["legal_aid_entitlement"]["body"]
