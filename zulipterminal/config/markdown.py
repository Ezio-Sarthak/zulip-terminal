from typing import List

from typing_extensions import TypedDict


class MarkdownElements(TypedDict):
    re_render_required: bool
    content: str
    raw_format: str
    html_format: str


MARKDOWN_ELEMENTS: List[MarkdownElements] = [
    {
        # BOLD TEXT
        "re_render_required": False,
        "content": "bold",
        "raw_format": "**{}**",
        "html_format": "<strong>{}</strong>",
    },
    {
        # EMOJI
        "re_render_required": False,
        "content": "heart",
        "raw_format": ":{}:",
        "html_format": '<span class="emoji">:{}:</span>',
    },
    {
        # MESSAGE LINKS
        "re_render_required": False,
        "content": "https://zulip.org",
        "raw_format": "[Zulip website]\n({})",
        "html_format": '<a href="{}">Zulip website</a>',
    },
    {
        # BULLET LISTS
        "re_render_required": False,
        "content": "",
        "raw_format": "* Milk\n* Tea\n  * Green tea\n  * Black tea\n"
        "  * Oolong tea\n* Coffee",
        "html_format": "<ul><li>Milk</li><li>Tea<ul><li>Green tea</li>"
        "<li>Black tea</li><li>Oolong tea</li></ul>"
        "</li><li>Coffee</li>",
    },
    {
        # NUMBERED LISTS
        "re_render_required": False,
        "content": "",
        "raw_format": "1. Milk\n2. Tea\n3. Coffee",
        "html_format": "<ol><li>Milk</li><li>Tea</li><li>Coffee</li></ol>",
    },
    {
        # USER MENTIONS
        "re_render_required": True,
        "content": "King Hamlet",
        "raw_format": "@**{}**",
        "html_format": '<span class="user-mention">@{}</span>',
    },
    {
        # USER SILENT MENTIONS
        "re_render_required": True,
        "content": "King Hamlet",
        "raw_format": "@_**{}**",
        "html_format": '<span class="user-mention silent">{}</span>',
    },
    {
        # NOTIFY ALL RECIPIENTS
        "re_render_required": False,
        "content": "all",
        "raw_format": "@**{}**",
        "html_format": '<span class="user-mention">@{}</span>',
    },
    {
        # LINK TO A STREAM
        "re_render_required": False,
        "content": "announce",
        "raw_format": "#**{}**",
        "html_format": '<a class="stream" data-stream-id="6" '
        'href="/#narrow/stream/6-announce">#{}</a>',
    },
    {
        # STATUS MESSAGE
        "re_render_required": True,
        "content": "King Hamlet",
        "raw_format": "/me is busy writing code.",
        "html_format": "<strong>{}</strong> is busy writing code.",
    },
    {
        # INLINE CODE
        "re_render_required": False,
        "content": "code",
        "raw_format": "Some inline `{}`",
        "html_format": "Some inline <code>{}</code>",
    },
    {
        # CODE BLOCK
        "re_render_required": False,
        "content": "def zulip():\n    print 'Zulip'",
        "raw_format": "```\n{}\n```",
        "html_format": '<div class="codehilite"><pre><span></span><code>\n{}</code>'
        "</pre></div>",
    },
    {
        # QUOTED TEXT
        "re_render_required": False,
        "content": "Quoted",
        "raw_format": ">{}",
        "html_format": "<blockquote>░ {}</blockquote>",
    },
    {
        # QUOTED BLOCK
        "re_render_required": False,
        "content": "Quoted block",
        "raw_format": "```quote\n{}\n```",
        "html_format": "<blockquote>\n░ {}</blockquote>",
    },
    {
        # TABLE RENDERING
        "re_render_required": False,
        "content": "",
        "raw_format": "|Name|Id|\n|--|--:|\n|Robert|1|\n|Mary|100|",
        "html_format": '<table><thead><tr><th align="left">Name</th>'
        '<th align="right">Id</th></tr></thead><tbody>'
        '<tr><td align="left">Robert</td><td align="right">1'
        '</td></tr><tr><td align="left">Mary</td>'
        '<td align="right">100</td></tr></tbody></table>',
    },
]
