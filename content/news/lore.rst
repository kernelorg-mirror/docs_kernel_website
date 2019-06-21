List archives on lore.kernel.org
================================

:category: Site news
:slug: lore
:date: 2018-12-12

You may access the archives of many Linux development mailing lists on
lore.kernel.org_. Most of them include a full archive of messages going
back several decades.

- `listing of currently hosted archives`_

If you would like to suggest another kernel development mailing list to
be included in this list, please follow the instructions on the
following wiki page:

- `Adding list archives to lore.kernel.org`_

Archiving software
------------------
The software managing the archive is called `Public Inbox`_ and offers
the following features:

- Fast, searchable web archives
- Atom feeds per list or per individual thread
- Downloadable mbox archives to make replying easy
- Git-backed archival mechanism you can clone and pull
- Read-only nntp gateway

We collected many list archives going as far back as 1998, and they are
now all available to anyone via a simple git clone. We would like to
extend our thanks to everyone who helped in this effort by donating
their personal archives.

Obtaining full list archives
----------------------------
Git clone URLs are provided at the bottom of each page. Note, that due
mailing list volume, list archives are sharded into multiple
repositories, each roughly 1GB in size. In addition to cloning from
lore.kernel.org, you may also access these repositories on
erol.kernel.org_.

Mirroring
~~~~~~~~~
You can continuously mirror the entire mailing list archive collection
by using the grokmirror_ tool. The following repos.conf file should get
you all you need::

    [lore.kernel.org]
    site = https://lore.kernel.org
    manifest = https://lore.kernel.org/manifest.js.gz
    toplevel = /path/to/your/local/folder
    mymanifest = /path/to/your/local/folder/manifest.js.gz
    pull_threads = 4

Please note, that you will require at least 20+ GB of local storage. The
mirroring process only replicates the git repositories themselves -- if
you want to use public-inbox with them, you will need to run
"``public-inbox-init``" and "``public-inbox-index``" to create the
database files required for public-inbox operation.

Linking to list discussions from commits
----------------------------------------
If you need to reference a mailing list discussion inside code comments
or in a git commit message, please use the "permalink" URL provided by
public-inbox. It is available in the headers of each displayed message
or thread discussion. Alternatively, you can use a generic message-id
redirector in the form:

- https://lore.kernel.org/r/message@id

That should display the message regardless in which mailing list archive
it's stored.


.. _lore.kernel.org: https://lore.kernel.org/lists.html
.. _erol.kernel.org: https://erol.kernel.org/
.. _`listing of currently hosted archives`: https://lore.kernel.org/lists.html
.. _`Adding list archives to lore.kernel.org`: https://korg.wiki.kernel.org/userdoc/lore
.. _`Public Inbox`: https://public-inbox.org/design_notes.html
.. _grokmirror: https://github.com/mricon/grokmirror
