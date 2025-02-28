import imaplib
import email
from email.header import decode_header
from lxml import etree
import argparse
import time


class GmailClient:
    def __init__(self):
        self.imap_server = "imap.gmail.com"
        self.imap_port = 993
        self.login_email_address = None   # "testqa.hsvqa@gmail.com"
        self.login_email_password = None  # "Rdl@12345"
        self.default_mailbox = "INBOX"
        self.search_criteria = None

    def get_verification_code(self):
        try:
            # Wait for 10 seconds to receive email
            time.sleep(10)

            # Connect to IMAP server
            imap_connection = imaplib.IMAP4_SSL(self.imap_server, self.imap_port)

            # Login to Gmail
            imap_connection.login(self.login_email_address, self.login_email_password)

            # Select inbox
            imap_connection.select(self.default_mailbox)

            # Search for email containing verification code
            verification_code = self._search_email_contains_code(imap_connection, self.search_criteria)
            retry_count = 12

            # Retry for 12 times, waiting 10 seconds between retries
            while retry_count > 0 and not verification_code:
                time.sleep(10)
                retry_count -= 1
                verification_code = self._search_email_contains_code(imap_connection, self.search_criteria)

            if verification_code:
                print(f"Success get code: {verification_code}")
            else:
                print("Verification code not found.")

        except imaplib.IMAP4.error as err:
            print(f"IMAP error: {err}")

        except Exception as err:
            print(f"Failed to get verification code -> {err}")

        finally:
            try:
                imap_connection.logout()
            except Exception as err:
                pass

    def _search_email_contains_code(self, imap_connection, search_criteria):
        verification_code = None

        # Search for emails matching the search criteria
        status, message_ids = imap_connection.search(None, search_criteria)
        message_id_list = message_ids[0].split()

        for message_id in message_id_list:
            status, message_data = imap_connection.fetch(message_id, "(RFC822)")

            # Parse email content
            email_message = email.message_from_bytes(message_data[0][1])

            # Extract verification code from email body
            if email_message.get_content_maintype() == "text" and email_message.get_content_type() == 'text/html':
                email_body = email_message.get_payload(decode=True).decode("utf-8")
                tree = etree.HTML(email_body)
                verification_code_elements = tree.xpath('//p[@class="code"]')
                
                if verification_code_elements:
                    verification_code = verification_code_elements[0].text  # Adjust XPath as needed
                break
            else:
                raise Exception("Email content type is not text/html")

        return verification_code


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--email", help="Email address of Gmail account", required=True)
    parser.add_argument("-p", "--password", help="Password or App-specific password of Gmail account", required=True)
    parser.add_argument("-t", "--to", help="Recipient email address for the verification email", required=True)
    args = parser.parse_args()

    gmail_client = GmailClient()

    gmail_client.login_email_address = args.email
    gmail_client.login_email_password = args.password

    # Set search criteria based on recipient email address
    gmail_client.search_criteria = f'(TO "{args.to}")'

    gmail_client.get_verification_code()
