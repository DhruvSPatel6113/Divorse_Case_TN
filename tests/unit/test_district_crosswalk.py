"""
Unit tests for DistrictCrosswalk.
"""

import pytest
from src.geography.district_crosswalk import DistrictCrosswalk


def test_crosswalk_clean_raw_name():
    crosswalk = DistrictCrosswalk()
    assert crosswalk.clean_raw_name("District - Thiruvallur (01)") == "Thiruvallur"
    assert crosswalk.clean_raw_name("District - Chennai (02)") == "Chennai"
    assert crosswalk.clean_raw_name("State - TAMIL NADU (33)") == "TAMIL NADU"
    assert crosswalk.clean_raw_name("Coimbatore") == "Coimbatore"


def test_crosswalk_standardization():
    crosswalk = DistrictCrosswalk()
    assert crosswalk.standardize("District - Thiruvallur (01)") == "Thiruvallur"
    assert crosswalk.standardize("madras") == "Chennai"
    assert crosswalk.standardize("trichy") == "Tiruchirappalli"
    assert crosswalk.standardize("kanchipuram") == "Kancheepuram"
    assert crosswalk.standardize("kanyakumari") == "Kanniyakumari"
    assert crosswalk.standardize("tuticorin") == "Thoothukkudi"
    assert crosswalk.standardize("ranipet") == "Ranipet"
    assert crosswalk.standardize("invalid_district_xyz") is None


def test_crosswalk_census_codes():
    crosswalk = DistrictCrosswalk()
    assert crosswalk.get_census_code("Chennai") == 2
    assert crosswalk.get_census_code("Coimbatore") == 31
    assert crosswalk.get_census_code("Thiruvallur") == 1
    assert crosswalk.get_census_code("Tiruppur") == 32
    # Ranipet was formed post-2011, so it has no 2011 code
    assert crosswalk.get_census_code("Ranipet") is None


def test_crosswalk_split_details():
    crosswalk = DistrictCrosswalk()
    vellore_split = crosswalk.get_split_details("Vellore")
    assert vellore_split["is_split_parent"] is True
    assert "Tirupattur" in vellore_split["children"]
    assert "Ranipet" in vellore_split["children"]

    ranipet_split = crosswalk.get_split_details("Ranipet")
    assert ranipet_split["is_split_parent"] is False
    assert ranipet_split["parent"] == "Vellore"

    salem_split = crosswalk.get_split_details("Salem")
    assert salem_split["is_split_parent"] is False
    assert salem_split["parent"] is None
    assert salem_split["split_period"] == "stable"


def test_crosswalk_all_32_districts():
    crosswalk = DistrictCrosswalk()
    districts = crosswalk.list_all_canonical_2011_districts()
    assert len(districts) == 32
    assert "Chennai" in districts
    assert "Madurai" in districts
    assert "Coimbatore" in districts
