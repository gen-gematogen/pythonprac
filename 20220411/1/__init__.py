import gettext

translation = gettext.translation("1", "po", fallback=True)
_, ngettext = translation.gettext, translation.ngettext

def dialog():
    while s := input(_("Input string: ")):
        print(ngettext("{} word enetered", "{} words entered", len(s.split())).format(len(s.split())))
