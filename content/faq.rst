Frequently asked questions
==========================

:slug: faq
:category: FAQ

If you have questions, comments or concerns about the F.A.Q. please
contact us at helpdesk@kernel.org.

Is Linux Kernel Free Software?
------------------------------
Linux kernel is released under the terms of GNU GPL version 2 and is
therefore Free Software as defined by the `Free Software Foundation`_.

For more information, please consult the documentation:

- `Linux kernel licensing rules`_

.. _`Free Software Foundation`: https://www.fsf.org/
.. _`Linux kernel licensing rules`: https://docs.kernel.org/process/license-rules.html

I heard that Linux ships with non-free "blobs"
----------------------------------------------
Before many devices are able to communicate with the OS, they must first
be initialized with the "firmware" provided by the device manufacturer.
This firmware is not part of Linux and isn't "executed" by the kernel --
it is merely uploaded to the device during the driver initialization
stage.

While some firmware images are built from free software, a large subset
of it is only available for redistribution in binary-only form. To
avoid any licensing confusion, firmware blobs were moved from the main
Linux tree into a separate repository called `linux-firmware`_.

It is possible to use Linux without any non-free firmware binaries, but
usually at the cost of rendering a lot of hardware inoperable.
Furthermore, many devices that do not require a firmware blob during
driver initialization simply already come with non-free firmware
preinstalled on them. If your goal is to run a 100% free-as-in-freedom
setup, you will often need to go a lot further than just avoiding
loadable binary-only firmware blobs.

.. _`linux-firmware`: https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/

Can I use the word "Linux" or the Tux logo?
-------------------------------------------
Linux is a registered trademark of Linus Torvalds and its use is
governed by the Linux Trademark Institute. Please consult the following
page for further information:

- `Trademark Usage`_

The Tux penguin logo was created by Larry Ewing using Gimp software. It
is free to use, including commercially, as long as you give Larry Ewing
proper credit ("if someone asks"). For any other permissions, please
reach out to Mr. Larry Ewing directly.

.. _`Trademark Usage`: https://www.linuxfoundation.org/trademark-usage/

What does "stable/EOL" and "longterm" mean?
-------------------------------------------
As kernels move from the "mainline" into the "stable" category, two
things can happen:

1. They can reach "End of Life" after a few bugfix revisions, which
   means that kernel maintainers will release no more bugfixes for this
   kernel version, or
2. They can be put into "longterm" maintenance, which means that
   maintainers will provide bugfixes for this kernel revision for a
   much longer period of time.

If the kernel version you are using is marked "EOL," you should consider
upgrading to the next major version as there will be no more bugfixes
provided for the kernel version you are using.

Please check the Releases_ page for more info.

.. _Releases: |filename|releases.rst

Why is an LTS kernel marked as "stable" on the front page?
----------------------------------------------------------
Long-term support ("LTS") kernels announced on the Releases_ page will
be marked as "stable" on the front page if there are no other current
stable kernel releases. This is done to avoid breaking automated parsers
monitoring kernel.org with an expectation that there will always be a
kernel release marked as "stable."

Linus has tagged a new release, but it's not listed on the front page!
----------------------------------------------------------------------
Linus Torvalds PGP-signs git repository tags for all new mainline kernel
releases, however a separate set of PGP signatures needs to be generated
by the stable release team in order to create downloadable tarballs. Due
to timezone differences between Linus and the members of the stable
team, there is usually a delay of several hours between when the new
mainline release is tagged and when PGP-signed tarballs become
available. The front page is updated once that process is completed.

Is there an RSS feed for the latest kernel version?
---------------------------------------------------
Yes, and you can find it at https://www.kernel.org/feeds/kdist.xml.

We also publish a .json file with the latest release information, which
you can pull from here: https://www.kernel.org/releases.json.

Where can I find kernel 3.10.0-1160.45.1.foo?
---------------------------------------------
Kernel versions that have a dash in them are packaged by distributions
and are often extensively modified. Please contact the relevant
distribution to obtain the exact kernel source.

See the Releases_ page for more info on distribution kernels.

.. _Releases: |filename|releases.rst

How do I report a problem with the kernel?
------------------------------------------
If you are running a kernel that came with your Linux distribution, then
the right place to start is by reporting the problem through your
distribution support channels. Here are a few popular choices:

- `Ubuntu <https://help.ubuntu.com/stable/ubuntu-help/report-ubuntu-bug.html.en>`_
- `Fedora Project <https://docs.fedoraproject.org/en-US/quick-docs/howto-file-a-bug/>`_
- `Arch Linux <https://bugs.archlinux.org/>`_
- `Linux Mint <https://projects.linuxmint.com/reporting-an-issue.html>`_
- `Debian GNU/Linux <https://www.debian.org/Bugs/Reporting>`_
- `Red Hat <https://bugzilla.redhat.com/>`_
- `OpenSUSE <https://bugzilla.opensuse.org/>`_
- `SUSE <https://bugzilla.suse.com/>`_

If you are sure that the problem is with the upstream kernel, please
refer to the following document that describes how to report bugs and
regressions to the developers:

- `Reporting issues`_

.. _`Reporting issues`: https://docs.kernel.org/admin-guide/reporting-issues.html

How do I get involved with Linux Kernel development?
----------------------------------------------------
A good place to start is the `Kernel Newbies`_ website.

.. _`Kernel Newbies`: http://kernelnewbies.org/

Can I get an account on kernel.org?
-----------------------------------
Kernel.org accounts are usually reserved for subsystem maintainers or
high-profile developers. It is absolutely not necessary to have an
account on kernel.org to contribute to the development of the Linux
kernel, unless you submit pull requests directly to Linus Torvalds.

If you are listed in the MAINTAINERS file or have reasons to believe you
should have an account on kernel.org because of the amount of your
contributions, please refer to the `accounts page`_ for the
procedure to follow.

.. _`accounts page`: https://korg.docs.kernel.org/accounts.html

