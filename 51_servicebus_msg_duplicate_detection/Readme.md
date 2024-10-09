# Azure Service Bus Duplicate detection

## Introduction

If an application fails due to a fatal error immediately after sending a message, and the restarted application instance erroneously believes that the prior message delivery didn't occur, a subsequent send causes the same message to appear in the system twice.

It's also possible for an error at the client or network level to occur a moment earlier, and for a sent message to be committed into the queue, with the acknowledgment not successfully returned to the client. This scenario leaves the client in doubt about the outcome of the send operation.

Duplicate detection takes the doubt out of these situations by enabling the sender resend the same message, and the queue or topic discards any duplicate copies.

## How it works

Enabling duplicate detection helps keep track of the application-controlled MessageId of all messages sent into a queue or topic during a specified time window. If any new message is sent with MessageId that was logged during the time window, the message is reported as accepted (the send operation succeeds), but the newly sent message is instantly ignored and dropped. No other parts of the message other than the MessageId are considered.

Application control of the identifier is essential, because only that allows the application to tie the MessageId to a business process context from which it can be predictably reconstructed when a failure occurs.

For a business process in which multiple messages are sent in the course of handling some application context, the MessageId can be a composite of the application-level context identifier, such as a purchase order number, and the subject of the message, for example, 12345.2017/payment.

The MessageId can always be some GUID, but anchoring the identifier to the business process yields predictable repeatability, which is desired for using the duplicate detection feature effectively.

## Duplicate detection window size

Apart from just enabling duplicate detection, you can also configure the size of the duplicate detection history time window during which message IDs are retained. This value defaults to 10 minutes for queues and topics, with a minimum value of 20 seconds to maximum value of 7 days.

Enabling duplicate detection and the size of the window directly impact the queue (and topic) throughput, since all recorded message IDs must be matched against the newly submitted message identifier.

Keeping the window small means that fewer message IDs must be retained and matched, and throughput is impacted less. For high throughput entities that require duplicate detection, you should keep the window as small as possible.

## Resources

https://learn.microsoft.com/en-us/azure/service-bus-messaging/duplicate-detection
https://learn.microsoft.com/en-us/azure/service-bus-messaging/enable-duplicate-detection