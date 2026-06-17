from typing import Type
from crewai.tools import BaseTool
from mailersend import EmailBuilder, MailerSendClient
from pydantic import BaseModel, Field
import os
import dotenv

dotenv.load_dotenv(override=True)


class EmailMessage(BaseModel):
    """A message to be sent to the user"""

    subject: str = Field(..., description="The subject of the email.")
    body: str = Field(..., description="The body of the email.")


class EmailTool(BaseTool):
    mailer_send_api_token: str = os.getenv("MAILER_SEND_API_TOKEN")
    mailer_send_domain: str = os.getenv("MAILER_SEND_DOMAIN")
    ms: MailerSendClient = MailerSendClient(api_key=mailer_send_api_token)
    your_email: str = os.getenv("YOUR_EMAIL")

    name: str = "Send an Email"
    description: str = "This tool is used to send an email to the user."
    args_schema: Type[BaseModel] = EmailMessage

    def _run(self, subject: str, body: str) -> str:
        print(
            f"Sending email to {self.your_email} with subject {subject} and body {body}"
        )
        email = (
            EmailBuilder()
            .from_email(f"stock_picker_agent@{self.mailer_send_domain}", "Stock Picker")
            .to_many([{"email": self.your_email}])
            .subject(subject)
            .text(body)
            .build()
        )
        response = self.ms.emails.send(email)
        message = f"Email sent: {response.id}"
        print(message)
        return message
