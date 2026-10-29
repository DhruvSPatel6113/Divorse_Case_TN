"""
Questionnaire Module for Public Relationship Reflection & Legal Process Guidance.

Complies with Section 8.A and Section 8.E:
- 100% optional answers with skip capability.
- Strict privacy: No PII (names, phones, emails, addresses, case numbers) collected or stored.
- Processed entirely in volatile memory; zero remote persistence.
"""

from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional


@dataclass
class QuestionnaireResponse:
    query_context: Optional[str] = None  # 'relationship_concerns', 'existing_case', 'general_information'
    concerns: List[str] = field(default_factory=list)
    concerns_discussed: Optional[str] = None  # 'yes', 'no', 'partially', 'prefer_not_to_say'
    discussion_safety: Optional[str] = None  # 'safe', 'somewhat_tense', 'unsafe_or_fearful', 'prefer_not_to_say'
    user_goal: Optional[str] = None  # 'reconciliation_pathways', 'separation_options', 'understand_legal_process', 'unsure'
    petition_filed: Optional[str] = None  # 'yes', 'no', 'considering', 'prefer_not_to_say'
    case_procedural_stage: Optional[str] = None  # 'pre_filing', 'notice_issued', 'mediation_counselling', 'evidence_hearings', 'awaiting_judgment', 'not_applicable'
    applicable_law: Optional[str] = None  # 'hindu_marriage_act', 'special_marriage_act', 'divorce_act_christian', 'muslim_personal_law', 'not_sure'
    proceedings_type: Optional[str] = None  # 'mutual_consent', 'contested', 'unsure'
    desired_resources: List[str] = field(default_factory=list)


CONCERN_OPTIONS = [
    "Communication breakdown",
    "Trust issues / Infidelity",
    "Recurring unresolved conflict",
    "Financial disagreement / Stress",
    "In-laws / Extended family interference",
    "Emotional distance / Incompatibility",
    "Intimidation, coercive control, or verbal abuse",
    "Physical safety concerns or domestic violence",
    "Parenting and child custody disagreements",
    "Other personal differences",
]

RESOURCE_OPTIONS = [
    "Marital & Family Counselling Services",
    "Court-Annexed Mediation Information",
    "Free Legal Aid (TNSLSA / DLSA Tamil Nadu)",
    "Domestic Violence & Emergency Support",
    "Mutual Consent Procedure Checklist",
    "Child Custody & Maintenance Guidelines",
]


class QuestionnaireManager:
    """Manages presentation and validation of the optional reflection questionnaire."""

    def __init__(self):
        self.concern_options = CONCERN_OPTIONS
        self.resource_options = RESOURCE_OPTIONS

    def validate_safety_flags(self, response: QuestionnaireResponse) -> bool:
        """Returns True if user indicates fear, intimidation, or safety concerns."""
        if response.discussion_safety == "unsafe_or_fearful":
            return True
        safety_concerns = [
            "Intimidation, coercive control, or verbal abuse",
            "Physical safety concerns or domestic violence",
        ]
        if any(c in response.concerns for c in safety_concerns):
            return True
        return False
