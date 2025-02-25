DEFAULT_ALLOWED_TAGS = [
    "p",
    "div",
    "span",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "tt",
    "pre",
    "em",
    "strong",
    "ul",
    "sup",
    "li",
    "dl",
    "dd",
    "dt",
    "code",
    "img",
    "a",
    "table",
    "tr",
    "th",
    "td",
    "tbody",
    "caption",
    "colgroup",
    "thead",
    "tfoot",
    "blockquote",
    "ol",
    "hr",
    "br",
]

DEFAULT_ALLOWED_ATTRIBUTES = {
    "*": [
        "class",
        "style",
        "id",
    ],
    "a": [
        "href",
        "target",
        "rel",
        "title",
    ],
    "img": [
        "src",
        "alt",
        "title",
    ],
    "tr": [
        "rowspan",
        "colspan",
    ],
    "td": [
        "rowspan",
        "colspan",
        "align",
    ],
}

DEFAULT_ALLOWED_STYLES = [
    "color",
    "background-color",
    "font-family",
    "font-weight",
    "font-size",
    "width",
    "height",
    "text-align",
    "border",
    "border-top",
    "border-bottom",
    "border-left",
    "border-right",
    "padding",
    "padding-top",
    "padding-bottom",
    "padding-left",
    "padding-right",
    "margin",
    "margin-top",
    "margin-bottom",
    "margin-left",
    "margin-right",
]

DEFAULT_BLEACH_KWARGS = {
    "tags": DEFAULT_ALLOWED_TAGS,
    "attributes": DEFAULT_ALLOWED_ATTRIBUTES,
    "styles": DEFAULT_ALLOWED_STYLES,
}

DEFAULT_IMAGE_OPTS = {
    "spec": "width-500",
    "classname": "left",
}

UNSAFE_HTML = False

WRAP_IMAGES_IN_ANCHORS = True

SETTINGS_MODE_OVERRIDE = "override"
