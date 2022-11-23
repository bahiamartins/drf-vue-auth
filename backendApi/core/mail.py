from django.core.mail import EmailMultiAlternatives, get_connection
from django.template.loader import get_template
from django.utils import timezone
from core.models import Message

def sendEmail(data, subject, from_email, to_email, cc=None, message_id=None):

    successId = []
    
    connection = get_connection()
    connection.open()

    htmly = get_template('emails/email.html')
    html_content = htmly.render(data)

    msg = EmailMultiAlternatives(
        subject,
        html_content,
        from_email,
        [to_email],
        [cc],
        connection=connection
    )
    msg.attach_alternative(html_content, "text/html")
    result = msg.send()

    if result == 1 and message_id is not None:
        successId.append(message_id)

    connection.close()  # Cleanup

    if successId:
        objs = Message.objects.filter(id__in=successId)
        objs.sent_at = timezone.now()
        Message.objects.abulk_update(objs, ['sent_at'])