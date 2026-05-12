class LapseSegment:
    """
    Represents a single lapse assumption segment.

    Pure data container:
    - no lookup logic
    - no projection logic

    Typically corresponds to one assumption row.
    """

    def __init__(
        self,
        product_type: str,
        smoker_status: str,
        duration_start: int,
        duration_end: int,
        lapse_rate: float
    ):

        self.product_type = product_type
        self.smoker_status = smoker_status
        self.duration_start = duration_start
        self.duration_end = duration_end
        self.lapse_rate = lapse_rate

    def matches(self, policy, duration: int) -> bool:
        """
        Determine whether this segment applies
        to the given policy and duration.
        """

        return (
            self.product_type == policy.product_type
            and self.smoker_status == policy.smoker_status
            and self.duration_start <= duration <= self.duration_end
        )

    def __repr__(self):

        return (
            f"LapseSegment("
            f"product_type={self.product_type}, "
            f"smoker_status={self.smoker_status}, "
            f"duration={self.duration_start}-{self.duration_end}, "
            f"lapse_rate={self.lapse_rate}"
            f")"
        )
    
class LapseTable:
    """
    Provider of lapse assumptions.

    Responsible for:
    - storing lapse segments
    - resolving applicable lapse rates

    Does NOT:
    - perform projection logic
    - read CSV files
    """

    def __init__(self, segments):

        self.segments = segments

    def lapse_rate(self, policy, t: int) -> float:
        """
        Return lapse rate for a policy at time t.
        """

        duration = t + 1

        for segment in self.segments:

            if segment.matches(policy, duration):

                return segment.lapse_rate

        return 0.0

    def __repr__(self):

        return (
            f"LapseTable("
            f"segments={len(self.segments)}"
            f")"
        )