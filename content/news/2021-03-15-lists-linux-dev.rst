Linux.dev mailing list service
==============================

:category: Site news
:author: Konstantin Ryabitsev
:slug: lists-linux-dev

We are pleased to announce the availability of a new mailing list
service running under the new `lists.linux.dev
<https://lists.linux.dev>`_ domain. The goal of this deployment is to
offer a subscription service that:

- prioritizes mail delivery to public-inbox archives available
  via `lore.kernel.org <https://lore.kernel.org>`_
- conforms to DMARC requirements to ensure subscriber delivery
- makes minimal changes to email headers and no changes to the message
  body content for the purposes of preserving patch attestation

If you would like to host a Linux development mailing list on this
platform, please see further details on the `subspace.kernel.org
<https://subspace.kernel.org>`_ site.

Why another mailing list service?
---------------------------------
Linux development started in 1991 and has been ongoing for the past 30
years at an ever-increasing pace. Many popular code collaboration
platforms have risen throughout these three decades -- and while some of
them are still around, many others have shut down and disappeared
without offering any way to preserve the history of the projects they
used to host.

Development via mailed-in patches remains the only widely used mechanism
for code collaboration that does not rely on centralized infrastructure
maintained by any single entity. The Linux developer community sees
transparency, independence and decentralization as core guiding
principles behind Linux development, so it has deliberately chosen to
continue using email for all its past and ongoing collaboration efforts.

What about vger.kernel.org?
---------------------------
The infrastructure behind lists.linux.dev supports multiple domains, so
all mailing lists hosted on vger.kernel.org will be carefully migrated
to the same platform while preserving current addresses, subscribers,
and list ids. The only thing that will noticeably change is the
procedure to subscribe and unsubscribe from individual lists. As
majordomo is no longer maintained, we will instead switch to using
separate subscribe/unsusbscribe addresses per each list.

There are no firm ETAs for this migration, but if you are currently
subscribed to any mailing list hosted on vger.kernel.org, you will
receive a message when the migration date is approaching.
