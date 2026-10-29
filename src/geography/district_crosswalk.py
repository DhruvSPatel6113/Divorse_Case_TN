"""
District Crosswalk Module for Tamil Nadu.

Manages district name standardization, 2011 Census codes (32 districts),
and subsequent bifurcations/trifurcations (up to 38 present districts).
Complies with Section 4.D: preserves source records and documents mapping confidence.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional
import re


@dataclass
class DistrictMapping:
    original_name: str
    standardized_name: str
    census_2011_code: Optional[int]
    present_district_code: Optional[str]
    validity_period: str
    is_parent_district: bool
    bifurcated_children: List[str]
    parent_district: Optional[str]
    confidence: float
    notes: str


# Canonical 32 districts of Tamil Nadu (Census 2011 definition)
CENSUS_2011_DISTRICTS: Dict[int, str] = {
    1: "Thiruvallur",
    2: "Chennai",
    3: "Kancheepuram",
    4: "Vellore",
    5: "Tiruvannamalai",
    6: "Viluppuram",
    7: "Salem",
    8: "Namakkal",
    9: "Erode",
    10: "The Nilgiris",
    11: "Dindigul",
    12: "Karur",
    13: "Tiruchirappalli",
    14: "Perambalur",
    15: "Ariyalur",
    16: "Cuddalore",
    17: "Nagapattinam",
    18: "Thiruvarur",
    19: "Thanjavur",
    20: "Pudukkottai",
    21: "Sivaganga",
    22: "Madurai",
    23: "Theni",
    24: "Virudhunagar",
    25: "Ramanathapuram",
    26: "Thoothukkudi",
    27: "Tirunelveli",
    28: "Kanniyakumari",
    29: "Dharmapuri",
    30: "Krishnagiri",
    31: "Coimbatore",
    32: "Tiruppur",
}

# Post-2018 Administrative Bifurcations in Tamil Nadu
# 1. Kancheepuram -> Kancheepuram, Chengalpattu (2019)
# 2. Vellore -> Vellore, Tirupattur, Ranipet (2019)
# 3. Viluppuram -> Viluppuram, Kallakurichi (2019)
# 4. Tirunelveli -> Tirunelveli, Tenkasi (2019)
# 5. Nagapattinam -> Nagapattinam, Mayiladuthurai (2020)
POST_2018_SPLITS: Dict[str, List[str]] = {
    "Kancheepuram": ["Kancheepuram", "Chengalpattu"],
    "Vellore": ["Vellore", "Tirupattur", "Ranipet"],
    "Viluppuram": ["Viluppuram", "Kallakurichi"],
    "Tirunelveli": ["Tirunelveli", "Tenkasi"],
    "Nagapattinam": ["Nagapattinam", "Mayiladuthurai"],
}

# Aliases and alternative spellings encountered in official data portals
DISTRICT_ALIASES: Dict[str, str] = {
    "thiruvallur": "Thiruvallur",
    "tiruvallur": "Thiruvallur",
    "chennai": "Chennai",
    "madras": "Chennai",
    "kancheepuram": "Kancheepuram",
    "kanchipuram": "Kancheepuram",
    "vellore": "Vellore",
    "tiruvannamalai": "Tiruvannamalai",
    "thiruvannamalai": "Tiruvannamalai",
    "viluppuram": "Viluppuram",
    "villupuram": "Viluppuram",
    "salem": "Salem",
    "namakkal": "Namakkal",
    "erode": "Erode",
    "the nilgiris": "The Nilgiris",
    "nilgiris": "The Nilgiris",
    "dindigul": "Dindigul",
    "karur": "Karur",
    "tiruchirappalli": "Tiruchirappalli",
    "trichy": "Tiruchirappalli",
    "tiruchirapalli": "Tiruchirappalli",
    "perambalur": "Perambalur",
    "ariyalur": "Ariyalur",
    "cuddalore": "Cuddalore",
    "nagapattinam": "Nagapattinam",
    "nagappattinam": "Nagapattinam",
    "thiruvarur": "Thiruvarur",
    "tiruvarur": "Thiruvarur",
    "thanjavur": "Thanjavur",
    "tanjore": "Thanjavur",
    "pudukkottai": "Pudukkottai",
    "pudukottai": "Pudukkottai",
    "sivaganga": "Sivaganga",
    "sivagangai": "Sivaganga",
    "madurai": "Madurai",
    "theni": "Theni",
    "virudhunagar": "Virudhunagar",
    "virudunagar": "Virudhunagar",
    "ramanathapuram": "Ramanathapuram",
    "ramnad": "Ramanathapuram",
    "thoothukkudi": "Thoothukkudi",
    "thoothukudi": "Thoothukkudi",
    "tuticorin": "Thoothukkudi",
    "tirunelveli": "Tirunelveli",
    "thirunelveli": "Tirunelveli",
    "kanniyakumari": "Kanniyakumari",
    "kanyakumari": "Kanniyakumari",
    "dharmapuri": "Dharmapuri",
    "krishnagiri": "Krishnagiri",
    "coimbatore": "Coimbatore",
    "kovai": "Coimbatore",
    "tiruppur": "Tiruppur",
    "tirupur": "Tiruppur",
    # Newly created districts
    "chengalpattu": "Chengalpattu",
    "chengalpet": "Chengalpattu",
    "tirupattur": "Tirupattur",
    "ranipet": "Ranipet",
    "kallakurichi": "Kallakurichi",
    "tenkasi": "Tenkasi",
    "mayiladuthurai": "Mayiladuthurai",
}


class DistrictCrosswalk:
    """Standardizes district names and provides historical split context."""

    def __init__(self):
        self.census_districts = CENSUS_2011_DISTRICTS
        self.splits = POST_2018_SPLITS
        self.aliases = DISTRICT_ALIASES

    def clean_raw_name(self, name: str) -> str:
        """Strip prefixes like 'District - ' or codes like '(01)'."""
        if not name or not isinstance(name, str):
            return ""
        # Remove patterns like 'District - Thiruvallur (01)' or 'State - TAMIL NADU (33)'
        cleaned = re.sub(r"^(?:District|State)\s*-\s*", "", name, flags=re.IGNORECASE)
        cleaned = re.sub(r"\s*\(\d+\)\s*$", "", cleaned)
        return cleaned.strip()

    def standardize(self, raw_name: str) -> Optional[str]:
        """Standardize a raw district name to its canonical spelling."""
        cleaned = self.clean_raw_name(raw_name)
        key = cleaned.lower()
        if key in self.aliases:
            return self.aliases[key]
        return None

    def get_census_code(self, standardized_name: str) -> Optional[int]:
        """Return 2011 Census district code (1 to 32) if applicable."""
        for code, name in self.census_districts.items():
            if name.lower() == standardized_name.lower():
                return code
        return None

    def get_split_details(self, standardized_name: str) -> Dict[str, any]:
        """Return parent/child relationship for post-2018 bifurcated districts."""
        # Check if this is a parent district that split
        if standardized_name in self.splits:
            return {
                "is_split_parent": True,
                "children": self.splits[standardized_name],
                "parent": None,
                "split_period": "2019-2020",
                "notes": f"Historical 2011 boundary split into {', '.join(self.splits[standardized_name])}.",
            }

        # Check if this is a child district carved out from a parent
        for parent, children in self.splits.items():
            if standardized_name in children and standardized_name != parent:
                return {
                    "is_split_parent": False,
                    "children": [],
                    "parent": parent,
                    "split_period": "2019-2020",
                    "notes": f"Carved out from historical district '{parent}' during 2019-2020 reorganizations.",
                }

        return {
            "is_split_parent": False,
            "children": [],
            "parent": None,
            "split_period": "stable",
            "notes": "District boundary unchanged between 2011 and present.",
        }

    def list_all_canonical_2011_districts(self) -> List[str]:
        """Return sorted list of all 32 canonical 2011 districts."""
        return sorted(list(self.census_districts.values()))
