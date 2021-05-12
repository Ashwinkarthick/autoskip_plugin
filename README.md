# autoskip_plugin

The plugin works with the cadnano2-pyqt5: feel free to modify it to other versions- it should be relatively straight forward.

Clone the autoinsert repository: git clone git@github.com:Ashwinkarthick/autoskip_plugin.git to the plugins folder inside the cadnano2-pyqt5 folder.
You can also download and manually place it inside cadnano2-pyqt5/plugins

One can also create a symbolic link if preferred.

The initial code was written by Juhana Kommeri as part of his master thesis "Computer-aided design software for custom nucleic acid nanostructures" in Aalto University (https://aaltodoc.aalto.fi/handle/123456789/23326).

The code was improved with help from Jaishankar Natarajan.

Autoinsert plugin is available at https://github.com/Ashwinkarthick/autoinsert_plugin


# How to use

The plugin has three options
1. target bps between skips      - number of base pairs between each skip site.
2. number of skips               - introduces specified number of skips at every target site (maximum 2)
3. minimum dist from edge        - distance from the initial edge crossover between the first two helices. 
