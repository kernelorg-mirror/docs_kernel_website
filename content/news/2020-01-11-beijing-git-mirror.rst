Git mirror available in Beijing
===============================

:category: Site news
:author: Konstantin Ryabitsev
:slug: beijing-git-mirror

If you are a developer located around Beijing, or if your connection to
Beijing is faster and more reliable than to locations outside of China,
then you may benefit from the new git.kernel.org mirror kindly provided
by `Code Aurora Forum`_ at https://kernel.source.codeaurora.cn/. This is
a full mirror that is updated just as frequently as other git.kernel.org
nodes (in fact, it is managed by the same team as the rest of kernel.org
infrastructure, since CAF is part of Linux Foundation IT projects).

To start using the Beijing mirror, simply clone from that location or
add a separate remote to your existing checkouts, e.g.::

    git remote add beijing git://kernel.source.codeaurora.cn/pub/scm/.../linux.git
    git fetch beijing master

You may also use http:// and https:// protocols if that makes it easier
behind corporate firewalls.

.. _`Code Aurora Forum`: https://www.codeaurora.org/
