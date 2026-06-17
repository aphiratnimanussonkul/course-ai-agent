from typing import Type
from crewai.tools import BaseTool
from mailersend import EmailBuilder, MailerSendClient
from pydantic import BaseModel, Field
import os
import dotenv

dotenv.load_dotenv(override=True)


class EmailMessage(BaseModel):
    """A message to be sent to the user"""

    to: str = Field(..., description="The email address of the recipient.")
    subject: str = Field(..., description="The subject of the email.")
    body: str = Field(..., description="The body of the email.")


class EmailTool(BaseTool):
    mailer_send_api_token: str = os.getenv("MAILER_SEND_API_TOKEN")
    mailer_send_domain: str = os.getenv("MAILER_SEND_DOMAIN")
    ms: MailerSendClient = MailerSendClient(api_key=mailer_send_api_token)

    name: str = "Send an Email"
    description: str = "This tool is used to send an email to the user."
    args_schema: Type[BaseModel] = EmailMessage

    def _run(self, to: str, subject: str, body: str) -> str:
        print(f"Sending email to {to} with subject {subject} and body {body}")
        email = (
            EmailBuilder()
            .from_email(f"sales@{self.mailer_send_domain}", "Sales Agent")
            .to_many([{"email": to}])
            .subject(subject)
            .body(body)
            .build()
        )
        response = self.ms.emails.send(email)
        message = f"Email sent: {response.id}"
        print(message)
        return message
