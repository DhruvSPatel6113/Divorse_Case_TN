"""
Legal Information and Procedural Guide Module for Tamil Nadu Family Courts.

Complies with Section 8.C:
- Verified Indian personal laws and judicial procedures:
  - Hindu Marriage Act, 1955 (HMA)
  - Special Marriage Act, 1954 (SMA)
  - Divorce Act, 1869 (Christian law)
  - Dissolution of Muslim Marriages Act, 1939 (DMMA)
  - Family Courts Act, 1984 (Central Act 66 of 1984)
  - Protection of Women from Domestic Violence Act, 2005 (PWDVA)
- Explains Mutual Consent vs Contested tracks, mediation, maintenance, child custody, and appeals.
- Strictly provides general legal educational information, not legal advice or outcome guarantees.
"""

from typing import Dict, Any, List, Optional


STATUTORY_PROVISIONS = {
    "hindu_marriage_act": {
        "statute_name": "Hindu Marriage Act, 1955",
        "jurisdiction": "Applies to Hindus, Buddhists, Jains, and Sikhs",
        "key_sections": [
            {"section": "Section 9", "topic": "Restitution of Conjugal Rights", "description": "Petition seeking reunion when one spouse has withdrawn without reasonable excuse."},
            {"section": "Section 10", "topic": "Judicial Separation", "description": "Formal legal separation releasing spouses from cohabitation obligation while preserving marriage bond."},
            {"section": "Section 12", "topic": "Voidable Marriages", "description": "Annulment grounds including non-consummation, fraud, or force."},
            {"section": "Section 13(1)", "topic": "Contested Divorce Grounds", "description": "Fault-based grounds: Cruelty (physical/mental), Desertion (>=2 years continuous), Adultery, Religious Conversion, Incurable Mental Disorder, Venereal Disease, Renunciation."},
            {"section": "Section 13B", "topic": "Divorce by Mutual Consent", "description": "Joint petition where spouses have lived separately for >=1 year and mutually agree to dissolve the marriage."},
            {"section": "Section 24", "topic": "Maintenance Pendente Lite", "description": "Interim maintenance and legal expense support for dependent spouse during litigation."},
            {"section": "Section 25", "topic": "Permanent Alimony & Maintenance", "description": "Lump-sum or periodic financial support awarded upon decree based on incomes and conduct."},
            {"section": "Section 26", "topic": "Custody of Minor Children", "description": "Interim and permanent orders for maintenance, education, and custody with child welfare as paramount."},
        ],
    },
    "special_marriage_act": {
        "statute_name": "Special Marriage Act, 1954",
        "jurisdiction": "Civil marriage secular statute applying regardless of religion or for interfaith unions",
        "key_sections": [
            {"section": "Section 27", "topic": "Contested Divorce", "description": "Grounds matching HMA including cruelty, desertion, adultery, and imprisonment."},
            {"section": "Section 28", "topic": "Divorce by Mutual Consent", "description": "Joint petition after 1 year of separate living."},
            {"section": "Sections 36 & 37", "topic": "Alimony and Maintenance", "description": "Interim and permanent financial provisions."},
        ],
    },
    "divorce_act_christian": {
        "statute_name": "Divorce Act, 1869 (as amended in 2001)",
        "jurisdiction": "Applies to Christian marriages in India",
        "key_sections": [
            {"section": "Section 10", "topic": "Dissolution of Marriage", "description": "Grounds including adultery, cruelty, desertion, and conversion."},
            {"section": "Section 10A", "topic": "Mutual Consent", "description": "Joint petition with 1-year separation requirement."},
        ],
    },
    "muslim_personal_law": {
        "statute_name": "Dissolution of Muslim Marriages Act, 1939 & Muslim Personal Law",
        "jurisdiction": "Applies to Muslim marriages in India",
        "key_sections": [
            {"section": "Section 2 DMMA 1939", "topic": "Judicial Dissolution by Wife", "description": "Grounds for Muslim woman: Husband missing 4 years, failure to maintain for 2 years, imprisonment, severe cruelty, impotency, failure to perform marital duties."},
            {"section": "Mubarat / Khula", "topic": "Consensual Separation", "description": "Mutual consent dissolution (Mubarat) or separation initiated by wife upon terms (Khula)."},
        ],
    },
}

PROCEDURAL_TRACKS = {
    "mutual_consent": {
        "name": "Mutual Consent Pathway (Sec 13B HMA / Sec 28 SMA)",
        "estimated_duration": "6 to 18 months (cooling-off waiver possible upon Supreme Court criteria)",
        "stages": [
            {
                "stage_number": 1,
                "title": "Joint Settlement Agreement & MOU",
                "details": "Couples mutually settle terms regarding division of assets, permanent alimony/maintenance, and child custody/visitation in a binding memorandum.",
            },
            {
                "stage_number": 2,
                "title": "Filing First Motion Petition",
                "details": "Joint original petition presented before the Family Court having jurisdiction (where marriage was solemnized, where couple last resided, or where wife resides).",
            },
            {
                "stage_number": 3,
                "title": "First Motion Hearing & Oath Recording",
                "details": "Both parties appear (physically or via video conference where permitted); statements recorded under oath.",
            },
            {
                "stage_number": 4,
                "title": "Statutory 6-Month Reflection Period ('Cooling-off')",
                "details": "Under Sec 13B(2), statute provides a 6-month period. Under SC precedent (Amardeep Singh v. Harveen Kaur), courts can waive this if all efforts to save marriage failed and terms are fully settled.",
            },
            {
                "stage_number": 5,
                "title": "Second Motion Hearing & Final Decree",
                "details": "Parties confirm mutual consent on second motion; judge verifies voluntariness and signs final decree of dissolution.",
            },
        ],
    },
    "contested": {
        "name": "Contested Litigation Pathway",
        "estimated_duration": "2 to 5+ years depending on court backlog, appeals, and witness cross-examination",
        "stages": [
            {
                "stage_number": 1,
                "title": "Original Petition Filing (HMOP / OP / OS)",
                "details": "Petitioner files petition stating verified statutory grounds (e.g. cruelty, desertion).",
            },
            {
                "stage_number": 2,
                "title": "Summons / Notice to Respondent",
                "details": "Court issues formal notice. Respondent enters appearance with counsel.",
            },
            {
                "stage_number": 3,
                "title": "Mandatory Conciliation & Mediation (Section 9 Family Courts Act)",
                "details": "Under Section 9 of the Family Courts Act 1984, the Family Court has a mandatory duty to endeavor to assist and persuade the parties to arrive at a settlement. Case is referred to court counsellor or mediation center.",
            },
            {
                "stage_number": 4,
                "title": "Interim Applications (Section 24 HMA / Custody)",
                "details": "Hearing on interim maintenance, litigation expenses, or temporary child visitation during trial.",
            },
            {
                "stage_number": 5,
                "title": "Written Statement & Framing of Issues",
                "details": "Respondent files detailed defense; judge frames formal disputed issues of fact and law.",
            },
            {
                "stage_number": 6,
                "title": "Trial & Evidence Recording",
                "details": "Petitioner and respondent examine and cross-examine witnesses with documentary evidence.",
            },
            {
                "stage_number": 7,
                "title": "Final Arguments & Judgment",
                "details": "Counsels argue merits; court pronounces judgment granting decree or dismissing petition.",
            },
            {
                "stage_number": 8,
                "title": "Appeal to High Court (Section 19 Family Courts Act)",
                "details": "Aggrieved party may appeal within 30 days to a Division Bench of the Madras High Court (no appeal lies against consent orders or interlocutory rulings).",
            },
        ],
    },
}


class LegalInformationGuide:
    """Provides structured, verified Indian legal framework details."""

    def __init__(self):
        self.statutes = STATUTORY_PROVISIONS
        self.tracks = PROCEDURAL_TRACKS

    def get_statutory_details(self, statute_key: str = "hindu_marriage_act") -> Dict[str, Any]:
        """Fetch verified statutory provisions for specific personal law."""
        return self.statutes.get(statute_key, self.statutes["hindu_marriage_act"])

    def get_procedural_track(self, track_type: str = "mutual_consent") -> Dict[str, Any]:
        """Fetch step-by-step procedural flowchart."""
        return self.tracks.get(track_type, self.tracks["mutual_consent"])

    def get_comprehensive_guide(
        self,
        statute_key: Optional[str] = "hindu_marriage_act",
        track_type: Optional[str] = "mutual_consent",
    ) -> Dict[str, Any]:
        """Synthesize tailored legal educational guide."""
        statute_info = self.get_statutory_details(statute_key or "hindu_marriage_act")
        track_info = self.get_procedural_track(track_type or "mutual_consent")

        return {
            "title": "Tamil Nadu Family Court Legal Information Guide",
            "statutory_framework": statute_info,
            "procedural_track": track_info,
            "family_courts_act_provisions": {
                "act": "Family Courts Act, 1984 (Central Act No. 66 of 1984)",
                "section_9": "Mandatory duty of Family Court to make endeavors for reconciliation or settlement before trial.",
                "section_13": "Right to legal representation: Litigant may engage counsel with court permission.",
                "section_19": "Appeals lie to Division Bench of the High Court of Madras within 30 days of judgment.",
            },
            "legal_aid_entitlement": {
                "body": "Tamil Nadu State Legal Services Authority (TNSLSA) & District Legal Services Authorities (DLSA)",
                "statutory_basis": "Legal Services Authorities Act, 1987 (Section 12)",
                "eligibility": "All women and children are entitled to free legal aid irrespective of income. Free panel advocates appointed at every Family Court.",
            },
            "landmark_precedents": [
                {
                    "citation": "Amardeep Singh v. Harveen Kaur (2017) 8 SCC 746",
                    "principle": "The 6-month cooling-off period under Section 13B(2) HMA is directory, not mandatory. Courts can waive it where parties have lived separately for >18 months and settlement terms are resolved.",
                },
                {
                    "citation": "Rajnesh v. Neha (2020) 13 SCC 510",
                    "principle": "Comprehensive guidelines for maintenance in matrimonial cases: both parties must file detailed Affidavits of Disclosure of Assets and Liabilities.",
                },
                {
                    "citation": "Shilpa Sailesh v. Varun Sreenivasan (2023) SCC OnLine SC 544",
                    "principle": "Constitution Bench ruled that Supreme Court under Article 142 can grant divorce on ground of irretrievable breakdown of marriage without waiting periods.",
                },
            ],
            "statutory_disclaimer": (
                "LEGAL NOTICE: This guide provides objective legal information derived from official Indian statutes "
                "and reported precedents. It is not individualized legal advice and cannot substitute for representation "
                "by an advocate enrolled with the Bar Council of Tamil Nadu and Puducherry."
            ),
        }
