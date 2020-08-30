# MAIL.EDIT.MAILER

Equivalent to clicking the Mailer button when mailer is attached to the
current workbook. Allows you to edit a PowerTalk mailer attached to the
active workbook

**Note**&nbsp;&nbsp;&nbsp;This function is available on Macintosh
computers with Microsoft Excel and Apple PowerTalk only.

**Syntax**

**MAIL.EDIT.MAILER**(to\_recipients, cc\_recipients, bcc\_recipients,
subject, enclosures, which\_address)

**MAIL.EDIT.MAILER**?(to\_recipients, cc\_recipients, bcc\_recipients,
subject, enclosures, which\_address)

To\_recipients&nbsp;&nbsp;&nbsp;&nbsp;is the name of the person to whom
you want to send the mail. The name should be given as text. To specify
more than one name, give the list of names as an array.

Cc\_recipients&nbsp;&nbsp;&nbsp;&nbsp;is the name of those recipients to
be carbon copied. A single name should be given as text. To specify more
than one name, give the list of names as an array.

Bcc\_recipients&nbsp;&nbsp;&nbsp;&nbsp;is the name of the recipients to
be added as blind carbon copies.

Subject&nbsp;&nbsp;&nbsp;&nbsp; is a text string containing the subject
text for the mail messages.

Enclosures&nbsp;&nbsp;&nbsp;&nbsp;is an array of strings specifying
enclosures as file names.

Which\_address&nbsp;&nbsp;&nbsp;&nbsp;indicates which type of address to
use, as a text string, specifying the address type for all recipients.
For example, "Fax".

**Remarks**

If there is no mailer, returns the \#VALUE\! error value.

**Related Functions**

[MAIL.DELETE.MAILER](MAIL.DELETE.MAILER.md)&nbsp;&nbsp;&nbsp;Adds a new PowerTalk mailer to the
active workbook

[MAIL.ADD.MAILER](MAIL.ADD.MAILER.md)&nbsp;&nbsp;&nbsp;Adds a new PowerTalk mailer to the
active workbook



Return to [README](README.md#M)

