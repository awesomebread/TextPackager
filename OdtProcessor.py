from odf.opendocument import OpenDocumentText, load

def getBaseDocument():
    return OpenDocumentText()

def merge(inputfile, textdoc):
    inputtextdoc = load(inputfile)

    # Need to make a copy of the list because addElement unlinks from the original
    for meta in inputtextdoc.meta.childNodes[:]:
        textdoc.meta.addElement(meta)

    for font in inputtextdoc.fontfacedecls.childNodes[:]:
        textdoc.fontfacedecls.addElement(font)

    for style in inputtextdoc.styles.childNodes[:]:
        textdoc.styles.addElement(style)

    for autostyle in inputtextdoc.automaticstyles.childNodes[:]:
        textdoc.automaticstyles.addElement(autostyle)

    for scripts in inputtextdoc.scripts.childNodes[:]:
        textdoc.scripts.addElement(scripts)

    for settings in inputtextdoc.settings.childNodes[:]:
        textdoc.settings.addElement(settings)

    for masterstyles in inputtextdoc.masterstyles.childNodes[:]:
        textdoc.masterstyles.addElement(masterstyles)

    for body in inputtextdoc.body.childNodes[:]:
        textdoc.body.addElement(body)

    textdoc.Pictures.update(inputtextdoc.Pictures)
    return textdoc