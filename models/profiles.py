from enum import Enum


class ProfileEnum(Enum):
    """
    ProfileEnum is an enum class that contains all the possible profiles
    """
    STUDENT = "Student"
    TEACHER = "Teacher"
    SCHOOL = "School"
    OWNER = "Owner"

    def id_a_valid_profile(self, profile: str) -> bool:
        """
        Check if a profile is valid
        :param profile:
        :return:
        """
        return profile in [e.value for e in ProfileEnum]
