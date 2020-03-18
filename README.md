# radioid_utils
Utilities for working with radioid.net data

Project intention is to provide a single application to run on a server to deal with all the automated fetching of radioid.net databases, as well as library functions to make lookups quick and easy.

Having multiple software packages (such as hblink and dmrlink) running on a server means multiple loads of the database into memory, even if they all read from the same source on disk.  And something needs to keep the database updated.  By moving this functionality to its own service, the hope is that those other programs can be leaner in terms of memory usage.  Additionally, any changes in database format does not require changing any of the code in those other programs, only updating this software.

More to come.
