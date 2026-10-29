"""
Relationship Reflection Module.

Complies with Section 8.B:
- Generates non-diagnostic reflection guidance based on voluntary responses.
- Explicitly prohibits numerical divorce probability calculation or partner profiling.
- Prioritizes emergency safety resources whenever abuse, coercion, or fear is indicated.
- Refrains from recommending joint counselling when interpersonal safety is compromised.
"""

from typing import Dict, Any, List, Optional
from src.assessment.questionnaire import QuestionnaireResponse, QuestionnaireManager


CONCERN_CATALOG: Dict[str, Dict[str, str]] = {
    "Communication breakdown": {
        "reflection_question": "When conversations turn tense, are both parties listening to understand or reacting defensively? Would neutral third-party facilitation help bridge misunderstandings?",
        "healthy_step": "Practice structured communication intervals (such as timed speaking without interruptions) before attempting to resolve sensitive topics.",
    },
    "Trust issues / Infidelity": {
        "reflection_question": "Has there been an honest acknowledgment of breached trust, and is there genuine mutual willingness and emotional capacity to engage in the long process of rebuilding it?",
        "healthy_step": "Explore whether transparent boundaries and verifiable accountability can be re-established with the guidance of a qualified relationship therapist.",
    },
    "Recurring unresolved conflict": {
        "reflection_question": "Do arguments repeatedly cycle through the same historical grievances without reaching mutual closure, compromise, or behavioral change?",
        "healthy_step": "Identify specific conflict triggers; agree on a mutually respected 20-minute de-escalation timeout whenever emotional flooding occurs.",
    },
    "Financial disagreement / Stress": {
        "reflection_question": "Are household finances and budgeting handled with mutual transparency, or are there mismatched spending priorities, undisclosed liabilities, or unilateral financial decisions?",
        "healthy_step": "Conduct a structured, non-judgmental joint review of monthly budgets, assets, and liabilities to agree on clear shared financial expectations.",
    },
    "In-laws / Extended family interference": {
        "reflection_question": "Have you and your partner established clear boundaries as an autonomous marital unit, distinct from extended family pressures and traditions?",
        "healthy_step": "Hold a candid discussion to define mutual boundaries that protect your core relationship while maintaining respectful, balanced family ties.",
    },
    "Emotional distance / Incompatibility": {
        "reflection_question": "Have shared core life values, emotional intimacy, or visions of the future drifted apart over time? Is there mutual desire and curiosity to reconnect?",
        "healthy_step": "Reflect on whether differences reflect normal lifestyle evolution or deep value incompatibilities, and dedicate intentional time for shared reconnection.",
    },
    "Intimidation, coercive control, or verbal abuse": {
        "reflection_question": "Do you find yourself 'walking on eggshells', altering daily behavior out of apprehension, or feeling isolated from your personal support network?",
        "healthy_step": "Prioritize your personal emotional well-being; seek confidential individual counselling or speak with an experienced advocate rather than attempting unassisted joint confrontation.",
    },
    "Physical safety concerns or domestic violence": {
        "reflection_question": "Has any situation escalated to physical threats, intimidation, destruction of possessions, or fear for bodily safety for yourself or your children?",
        "healthy_step": "Prioritize physical safety above all else. Contact 24/7 emergency helplines (181 / 112) or the District Protection Officer to formulate a confidential personal safety plan.",
    },
    "Parenting and child custody disagreements": {
        "reflection_question": "Are differing parenting styles or marital conflicts creating an unstable emotional environment for your children, or drawing them into adult disagreements?",
        "healthy_step": "Adopt child-centric co-parenting principles; keep children completely insulated from marital disputes and consult a family mediator to structure clear parenting arrangements.",
    },
    "Other personal differences": {
        "reflection_question": "Are current stresses tied to career transitions, differing personal rhythms, cultural adjustments, or evolving individual life expectations?",
        "healthy_step": "Maintain a personal reflective journal for two weeks to clarify your core non-negotiable needs versus areas where flexible compromise is realistic.",
    },
}

CONTEXT_GUIDANCE: Dict[str, Dict[str, str]] = {
    "relationship_concerns": {
        "title": "🌱 Reflective Self-Assessment Stage",
        "guidance": (
            "You are reflecting on interpersonal dynamics before entering formal legal channels. "
            "This stage is best utilized to gain clarity on personal boundaries, explore whether differences can be resolved "
            "through constructive communication or counselling, and avoid making irreversible legal commitments during periods of peak emotional distress."
        ),
    },
    "existing_case": {
        "title": "⚖️ Active Court Docket Navigation Stage",
        "guidance": (
            "Because an official legal petition has already been initiated in the family court system, your immediate priorities include "
            "understanding mandatory court-annexed mediation (TNMCC), organizing required statutory documentation (marriage registration certificates, "
            "financial disclosure affidavits per Supreme Court guidelines), and safeguarding your individual legal rights."
        ),
    },
    "general_information": {
        "title": "📚 Legal & Demographic Research Stage",
        "guidance": (
            "You are reviewing educational information on Indian family law statutes and institutional procedures. "
            "This portal provides verified insights into statutory frameworks (HMA, Special Marriage Act, Christian Divorce Act, Muslim Personal Law), "
            "timelines, and public legal aid services available across Tamil Nadu."
        ),
    },
}

SAFETY_CLIMATE_GUIDANCE: Dict[str, str] = {
    "safe": (
        "Communication between partners remains physically and emotionally secure. When basic safety is intact, "
        "joint dialogue, open marital therapy, or pre-litigation conciliation offer practical, collaborative avenues for resolution."
    ),
    "somewhat_tense": (
        "Discussions frequently involve defensiveness, tension, or frustration. In this climate, unassisted direct confrontations "
        "often escalate. Working with a neutral, certified family mediator or individual counsellor can provide structured containment."
    ),
    "unsafe_or_fearful": (
        "Your responses indicate feelings of fear, intimidation, or safety concerns. "
        "When safety or domestic violence is an issue, joint confrontation or joint marriage counselling "
        "is NOT recommended as it may escalate risk. Please prioritize your physical and emotional wellbeing."
    ),
    "prefer_not_to_say": (
        "If you have any uncertainty regarding physical or emotional safety, err on the side of caution. "
        "Confidential support hotlines (181 / 112) are accessible 24/7 across Tamil Nadu without requiring any formal filing."
    ),
}

GOAL_PATHWAYS: Dict[str, List[str]] = {
    "reconciliation_pathways": [
        "Explore accredited couples counselling with a licensed clinical psychologist or family therapist to address underlying attachment dynamics.",
        "Consider voluntary pre-litigation conciliation at the District Legal Services Authority (DLSA) before filing contentious court petitions.",
        "Establish concrete, mutual milestones (e.g., a 90-day trial period of structured communication) to evaluate whether positive behavioral changes are sustainable.",
    ],
    "separation_options": [
        "Understand Judicial Separation: Under Section 10 of the Hindu Marriage Act (and equivalent statutes), judicial separation permits spouses to live apart while maintaining marital status and statutory inheritance/maintenance protections.",
        "Consider an informal trial separation agreement covering separate living arrangements, interim financial contributions, and structured children's schedules.",
        "Consult a matrimonial lawyer to ensure that living apart is documented amicably by consent to avoid allegations of unilateral desertion.",
    ],
    "understand_legal_process": [
        "Familiarize yourself with mandatory procedural stages: Petition filing -> Summons service -> Section 9 Family Courts Act conciliation/mediation -> Written statement -> Evidence trial -> Final judgment.",
        "Assess Mutual Consent vs. Contested Track: Mutual consent (e.g. HMA Section 13B) typically resolves within 6-18 months with significantly reduced emotional and financial strain compared to contested litigation (averaging 3-5+ years in Tamil Nadu Family Courts).",
        "Prepare foundational documentation, including marriage registration certificates, proof of residence, and comprehensive asset/liability disclosure affidavits mandated by the Supreme Court (Rajnesh v. Neha, 2020).",
    ],
    "unsure": [
        "Ambivalence is very common during marital distress. Consider 'Discernment Counselling'—a specialized short-term protocol (1-5 sessions) specifically designed for couples where one partner is leaning out and the other wishes to preserve the marriage.",
        "Implement an intentional 60 to 90-day decision pause: agree to refrain from issuing ultimatums or making sudden court filings while you gather clarity.",
        "Seek confidential, individual therapy to separate temporary reactive emotions (exhaustion, anger) from deep-seated, permanent incompatibilities.",
    ],
}


class RelationshipReflectionEngine:
    def __init__(self):
        self.manager = QuestionnaireManager()

    def generate_reflection_report(self, response: QuestionnaireResponse) -> Dict[str, Any]:
        """Synthesize non-diagnostic reflection, questions for personal consideration, and safety guidance."""
        has_safety_concern = self.manager.validate_safety_flags(response)

        # 1. Safety Alerts and Emergency Pathways
        safety_guidance = None
        if has_safety_concern:
            safety_guidance = {
                "priority_status": "URGENT_SAFETY_PRIORITY",
                "headline": "Personal Safety and Protective Support Comes First",
                "advisory": (
                    "Your responses indicate feelings of fear, intimidation, or safety concerns. "
                    "When safety or domestic violence is an issue, joint confrontation or joint marriage counselling "
                    "is NOT recommended as it may escalate risk. Please prioritize your physical and emotional wellbeing."
                ),
                "official_support_contacts": [
                    {"service": "Women Helpline (Tamil Nadu, 24/7 Toll-Free)", "contact": "181"},
                    {"service": "National Emergency Response Support System (ERSS)", "contact": "112"},
                    {"service": "Tamil Nadu State Legal Services Authority (TNSLSA) Free Legal Aid", "contact": "044-25342441 / 15100"},
                    {"service": "Tamil Nadu State Commission for Women (Chennai)", "contact": "044-28592750"},
                    {"service": "District Protection Officers (PWDVA)", "contact": "Available in all 38 District Collectorates"},
                ],
            }

        # 2. Context-specific guidance
        ctx_key = response.query_context or "relationship_concerns"
        context_info = CONTEXT_GUIDANCE.get(ctx_key, CONTEXT_GUIDANCE["relationship_concerns"])

        # 3. Discussion climate guidance
        safety_key = response.discussion_safety or "safe"
        climate_guidance = SAFETY_CLIMATE_GUIDANCE.get(safety_key, SAFETY_CLIMATE_GUIDANCE["safe"])

        # 4. Reflection Themes based on selected concerns (supports all 10 concerns)
        themes = []
        for concern in response.concerns:
            matched = False
            for catalog_concern, content in CONCERN_CATALOG.items():
                if catalog_concern.lower() in concern.lower() or any(
                    word in concern.lower() for word in catalog_concern.lower().split() if len(word) > 4
                ):
                    themes.append({
                        "concern": concern,
                        "reflection_question": content["reflection_question"],
                        "healthy_step": content["healthy_step"],
                    })
                    matched = True
                    break
            if not matched:
                themes.append({
                    "concern": concern,
                    "reflection_question": f"How does '{concern}' influence your emotional peace and vision for your partnership over the long term?",
                    "healthy_step": "Dedicate quiet time for individual reflection or consult an accredited relationship advisor.",
                })

        # 5. Goal pathways
        goal_key = response.user_goal or "unsure"
        goal_guidance = GOAL_PATHWAYS.get(goal_key, GOAL_PATHWAYS["unsure"])

        # 6. Dynamically synthesized recommendations based on exact combination of inputs
        dynamic_recs: List[str] = []

        # (a) Safety-driven recommendations
        if has_safety_concern:
            dynamic_recs.append(
                "Immediate Safety Priority: Reach out to the 24/7 Tamil Nadu Women Helpline (181) or ERSS (112) "
                "to discuss safe housing and emergency support before taking any confrontational steps."
            )
            dynamic_recs.append(
                "Protective Remedies: Review rights under the Protection of Women from Domestic Violence Act (PWDVA), 2005, "
                "including protection orders and residence orders through your local Protection Officer or Magistrate Court."
            )

        # (b) Concern-driven recommendations
        concerns_text = " ".join(response.concerns).lower()
        if "parenting" in concerns_text or "custody" in concerns_text or "child" in concerns_text:
            dynamic_recs.append(
                "Child Welfare Safeguard: Under Section 26 of the Hindu Marriage Act and settled Supreme Court precedent, "
                "custody decisions adhere strictly to the 'paramount welfare of the child' doctrine. Shield minor children from parental conflict and consider specialized child mediation."
            )

        if "financial" in concerns_text or "debt" in concerns_text or "money" in concerns_text:
            dynamic_recs.append(
                "Financial Record Transparency: Assemble transparent documentation of bank statements, tax filings, and liabilities. "
                "In legal maintenance inquiries, both parties are mandated by the Supreme Court (Rajnesh v. Neha, 2020) to submit exhaustive asset and liability disclosure affidavits."
            )

        if "in-laws" in concerns_text or "family" in concerns_text:
            dynamic_recs.append(
                "Marital Unit Boundary Setting: Seek joint or individual counseling focused specifically on establishing healthy boundaries "
                "between your nuclear marital unit and extended family demands."
            )

        if "trust" in concerns_text or "infidelity" in concerns_text:
            dynamic_recs.append(
                "Trust Reconstruction Assessment: True reconciliation requires transparent verification over a 6 to 12 month timeframe; "
                "if mutual transparency cannot be sustained, evaluate structured, dignified separation options."
            )

        if "communication" in concerns_text or "conflict" in concerns_text:
            dynamic_recs.append(
                "Communication Facilitation: When discussions become repetitive or defensive, introduce a neutral third party "
                "(such as a certified family mediator or marriage therapist) rather than continuing unassisted debates."
            )

        if "other personal differences" in concerns_text or "incompatibility" in concerns_text:
            dynamic_recs.append(
                "Core Value Clarification: Distinguish between resolvable differences in lifestyle habits and fundamental incompatibilities in life values, family visions, or personal ethics."
            )

        # (c) Context-driven recommendations
        if response.query_context == "existing_case":
            dynamic_recs.append(
                "Court-Annexed Mediation (TNMCC): Under Section 9 of the Family Courts Act, 1984, family courts mandatorily refer matters to mediation. "
                "Engage sincerely in court-annexed mediation; roughly 25-30% of cases achieve peaceful resolution without prolonged litigation."
            )
            dynamic_recs.append(
                "Free Legal Aid Entitlement: If you earn under statutory income limits or are a woman/child, you are entitled to free legal representation "
                "through the Tamil Nadu State Legal Services Authority (TNSLSA Helpline: 15100)."
            )
        elif response.query_context == "general_information":
            dynamic_recs.append(
                "Statutory Literacy: Compare mutual consent proceedings (Section 13B HMA / Section 28 SMA) against contested fault grounds (Section 13(1) HMA) "
                "using the Legal Process & Rights Guide tab to understand filing timelines and cooling-off waivers."
            )

        # (d) Climate-driven recommendations
        if response.discussion_safety == "somewhat_tense":
            dynamic_recs.append(
                "De-escalation in Communication: Shift sensitive discussions from informal private arguments into structured, moderated conversations in neutral settings."
            )

        # (e) Baseline foundational recommendation if list is short
        if len(dynamic_recs) < 3:
            dynamic_recs.append("Take deliberate time for reflection before initiating irrevocable legal procedures.")
            dynamic_recs.append("Seek guidance from licensed family therapists or registered matrimonial legal practitioners.")
            dynamic_recs.append("Ensure personal safety and the wellbeing of any minor children are kept paramount.")

        return {
            "title": "Relationship Reflection Summary",
            "is_diagnostic": False,
            "disclaimer": (
                "IMPORTANT NOTICE: This reflection guide is an informational tool, not clinical therapy, "
                "psychological diagnosis, or legal representation. It does not calculate divorce probability or infer partner intent."
            ),
            "safety_guidance": safety_guidance,
            "context_guidance": context_info,
            "safety_climate": climate_guidance,
            "selected_concerns_count": len(response.concerns),
            "reflection_themes": themes,
            "goal_pathways": goal_guidance,
            "general_recommendations": dynamic_recs,
        }
