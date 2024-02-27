from    disability_assistant \
        import  DisabilityAssistant

################################################################################
# Modify here to import your plugins.
from    plugins.color_disability.color_disability \
        import  ColorDisability
################################################################################

if  __name__ == "__main__":
    disability_assitant = DisabilityAssistant()
    ############################################################################
    # Modify here to enable/disable your plugins.
    disability_assitant.plugin_master.togglePlugin(ColorDisability())
    ############################################################################

    disability_assitant.start()