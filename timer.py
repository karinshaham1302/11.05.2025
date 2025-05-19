from datetime import datetime


class Timer:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
        self.started_at = datetime.now()

    def __str__(self) -> str:
        time_str = self.started_at.strftime("%H:%M:%S")
        return f"timer '{self.name}' set for {self.duration} minutes (started at: {time_str})"


    # def __repr__(self):
    #     return self.__str__()

    def __repr__(self):
        return f"timer('{self.name}', {self.duration})"

    def __del__(self):
        print(f"a goodbye message with timer name: '{self.name}' is being removed.")


# 6. לא למדנו





