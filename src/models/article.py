from dataclasses import dataclass

@dataclass(frozen=True)
class Article:
    title: str
    summary: str
    url: str

    def create_message(self) -> str:
        summary_limit = 200
        truncated_summary = self.summary[:summary_limit] if len(self.summary) > summary_limit else self.summary

        return f'''
        [{self.title}]
        {truncated_summary}
        詳しくはこちら
        {self.url}
        '''