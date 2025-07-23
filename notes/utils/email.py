from django.core.mail import send_mail
from django.conf import settings

def send_invitation_email(invitation):
    link = f"{settings.FRONTEND_URL}/accept-invitation/{invitation.token}/"
    subject = f"{invitation.invited_by.username} has invited you to collaborate on a notebook"
    message = (
        f"Hello,\n\n"
        f"You have been invited to collaborate on the notebook '{invitation.notebook.name}'.\n\n"
        f"Click the following link to accept the invitation:\n{link}\n\n"
        f"If you were not expecting this email, you can safely ignore it."
    )

    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [invitation.email])
