Customisable Multi-Column Order View
==========================

This is a plugin for `pretix`_.

Development setup
-----------------

1. Make sure that you have a working `pretix development setup`_.

2. Clone this repository, eg to ``local/pretix-cmcov``.

3. Activate the virtual environment you use for pretix development.

4. Execute ``python setup.py develop`` within this directory to register this application with pretix's plugin registry.

5. Execute ``make`` within this directory to compile translations.

6. Restart your local pretix server. You can now use the plugin from this repository for your events by enabling it in
   the 'plugins' tab in the settings.


License
-------

Part of the view and template code is heavily based on code from `pretix`_, which is also licensed under the Apache License 2.0. See their `AUTHORS`_ file for a list of all the awesome folks who contributed to pretix.

Copyright 2020 Karl Engelhardt

Released under the terms of the Apache License 2.0



.. _pretix: https://github.com/pretix/pretix
.. _pretix development setup: https://docs.pretix.eu/en/latest/development/setup.html
.. _AUTHORS: https://github.com/pretix/pretix/blob/master/AUTHORS
