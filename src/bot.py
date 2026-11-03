"""
Incident Response ChatOps Engine
Author: Vishwjeet Kumar Mehta
"""

import os
import logging
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from k8s_client import diagnose_failing_pods

logging.basicConfig(level=logging.INFO)

def handle_slash_command(command: str, channel_id: str, client: WebClient):
    """Processes /sre triage and /sre restart commands."""
    if command.startswith("/sre triage"):
        namespace = command.split(" ")[-1] if len(command.split(" ")) > 2 else "production"
        triage_report = diagnose_failing_pods(namespace)
        
        try:
            client.chat_postMessage(
                channel=channel_id,
                text=f"🚨 *SRE Incident Triage Report for `{namespace}`*",
                blocks=[
                    {
                        "type": "section",
                        "text": {"type": "mrkdwn", "text": f"```{triage_report}```"}
                    }
                ]
            )
        except SlackApiError as e:
            logging.error(f"Slack API error: {e}")

if __name__ == "__main__":
    token = os.getenv("SLACK_BOT_TOKEN", "mock-token")
    client = WebClient(token=token)
    print("ChatOps Incident Response Bot Initialized.")
