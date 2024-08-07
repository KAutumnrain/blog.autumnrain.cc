# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1723018120.1046777
_enable_loop = True
_template_filename = 'themes/bootblog4/templates/index.tmpl'
_template_uri = 'index.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content', 'content_header', 'before_content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='index_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('math', context._clean_inheritance_tokens(), templateuri='math_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'math')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('pagination', context._clean_inheritance_tokens(), templateuri='pagination_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'pagination')] = ns

    ns = runtime.TemplateNamespace('feeds_translations', context._clean_inheritance_tokens(), templateuri='feeds_translations_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'feeds_translations')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        multiple_authors_per_post = _import_ns.get('multiple_authors_per_post', context.get('multiple_authors_per_post', UNDEFINED))
        helper = _mako_get_namespace(context, 'helper')
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        def before_content():
            return render_before_content(context._locals(__M_locals))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        def content_header():
            return render_content_header(context._locals(__M_locals))
        page_links = _import_ns.get('page_links', context.get('page_links', UNDEFINED))
        featured = _import_ns.get('featured', context.get('featured', UNDEFINED))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        theme_config = _import_ns.get('theme_config', context.get('theme_config', UNDEFINED))
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        prevlink = _import_ns.get('prevlink', context.get('prevlink', UNDEFINED))
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        index_teasers = _import_ns.get('index_teasers', context.get('index_teasers', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        author_pages_generated = _import_ns.get('author_pages_generated', context.get('author_pages_generated', UNDEFINED))
        index_file = _import_ns.get('index_file', context.get('index_file', UNDEFINED))
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        nextlink = _import_ns.get('nextlink', context.get('nextlink', UNDEFINED))
        prev_next_links_reversed = _import_ns.get('prev_next_links_reversed', context.get('prev_next_links_reversed', UNDEFINED))
        front_index_header = _import_ns.get('front_index_header', context.get('front_index_header', UNDEFINED))
        pagination = _mako_get_namespace(context, 'pagination')
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context._locals(__M_locals))
        is_frontmost_index = _import_ns.get('is_frontmost_index', context.get('is_frontmost_index', UNDEFINED))
        math = _mako_get_namespace(context, 'math')
        current_page = _import_ns.get('current_page', context.get('current_page', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        pagekind = _import_ns.get('pagekind', context.get('pagekind', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'before_content'):
            context['self'].before_content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        def extra_head():
            return render_extra_head(context)
        index_file = _import_ns.get('index_file', context.get('index_file', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        math = _mako_get_namespace(context, 'math')
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n')
        if posts and (permalink == '/' or permalink == '/' + index_file):
            __M_writer('        <link rel="prefetch" href="')
            __M_writer(str(posts[0].permalink()))
            __M_writer('" type="text/html">\n')
        __M_writer('    ')
        __M_writer(str(math.math_styles_ifposts(posts)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        multiple_authors_per_post = _import_ns.get('multiple_authors_per_post', context.get('multiple_authors_per_post', UNDEFINED))
        helper = _mako_get_namespace(context, 'helper')
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        def content_header():
            return render_content_header(context)
        prev_next_links_reversed = _import_ns.get('prev_next_links_reversed', context.get('prev_next_links_reversed', UNDEFINED))
        front_index_header = _import_ns.get('front_index_header', context.get('front_index_header', UNDEFINED))
        pagination = _mako_get_namespace(context, 'pagination')
        page_links = _import_ns.get('page_links', context.get('page_links', UNDEFINED))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        comments = _mako_get_namespace(context, 'comments')
        prevlink = _import_ns.get('prevlink', context.get('prevlink', UNDEFINED))
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        index_teasers = _import_ns.get('index_teasers', context.get('index_teasers', UNDEFINED))
        def content():
            return render_content(context)
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        author_pages_generated = _import_ns.get('author_pages_generated', context.get('author_pages_generated', UNDEFINED))
        math = _mako_get_namespace(context, 'math')
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        current_page = _import_ns.get('current_page', context.get('current_page', UNDEFINED))
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        pagekind = _import_ns.get('pagekind', context.get('pagekind', UNDEFINED))
        nextlink = _import_ns.get('nextlink', context.get('nextlink', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_header'):
            context['self'].content_header(**pageargs)
        

        __M_writer('\n')
        if 'main_index' in pagekind:
            __M_writer('        ')
            __M_writer(str(front_index_header))
            __M_writer('\n')
        if page_links:
            __M_writer('        ')
            __M_writer(str(pagination.page_navigation(current_page, page_links, prevlink, nextlink, prev_next_links_reversed)))
            __M_writer('\n')
        __M_writer('    <div class="postindex">\n')
        for post in posts:
            __M_writer('            <article class="h-entry post-')
            __M_writer(str(post.meta('type')))
            __M_writer('" itemscope="itemscope" itemtype="http://schema.org/Article">\n            <header>\n                <h1 class="p-name entry-title"><a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" class="u-url">')
            __M_writer(filters.html_escape(str(post.title())))
            __M_writer('</a></h1>\n                <div class="metadata">\n                    <p class="byline author vcard"><span class="byline-name fn" itemprop="author">\n')
            if author_pages_generated and multiple_authors_per_post:
                pass
                for author in post.authors():
                    __M_writer('                            <a href="')
                    __M_writer(str(_link('author', author)))
                    __M_writer('">')
                    __M_writer(filters.html_escape(str(author)))
                    __M_writer('</a>\n')
            elif author_pages_generated:
                __M_writer('                        <a href="')
                __M_writer(str(_link('author', post.author())))
                __M_writer('">')
                __M_writer(filters.html_escape(str(post.author())))
                __M_writer('</a>\n')
            else:
                __M_writer('                        ')
                __M_writer(filters.html_escape(str(post.author())))
                __M_writer('\n')
            __M_writer('                    </span></p>\n            <p class="dateline">\n            <a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" rel="bookmark">\n            <time class="published dt-published" datetime="')
            __M_writer(str(post.formatted_date('webiso')))
            __M_writer('" itemprop="datePublished" title="')
            __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
            __M_writer('">')
            __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
            __M_writer('</time>\n')
            if post.updated and post.updated != post.date:
                __M_writer('                <span class="updated"> (')
                __M_writer(str(messages("updated")))
                __M_writer('\n                    <time class="dt-updated" datetime="')
                __M_writer(str(post.formatted_updated('webiso')))
                __M_writer('" itemprop="dateUpdated" title="')
                __M_writer(filters.html_escape(str(post.formatted_updated(date_format))))
                __M_writer('">')
                __M_writer(filters.html_escape(str(post.formatted_updated(date_format))))
                __M_writer('</time>)</span>\n')
            __M_writer('            </a>\n            </p>\n')
            if not post.meta('nocomments') and site_has_comments:
                __M_writer('                        <p class="commentline">')
                __M_writer(str(comments.comment_link(post.permalink(), post._base_path)))
                __M_writer('\n')
            __M_writer('                </div>\n            </header>\n')
            if index_teasers:
                __M_writer('                <div class="p-summary entry-summary">\n                    ')
                __M_writer(str(post.text(teaser_only=True)))
                __M_writer('\n                </div>\n')
            else:
                __M_writer('                <div class="e-content entry-content">\n                    ')
                __M_writer(str(post.text(teaser_only=False)))
                __M_writer('\n                </div>\n')
            __M_writer('            </article>\n')
        __M_writer('    </div>\n    ')
        __M_writer(str(helper.html_pager()))
        __M_writer('\n    ')
        __M_writer(str(comments.comment_link_script()))
        __M_writer('\n    ')
        __M_writer(str(math.math_scripts_ifposts(posts)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        def content_header():
            return render_content_header(context)
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        __M_writer = context.writer()
        __M_writer('\n        ')
        __M_writer(str(feeds_translations.translation_link(kind)))
        __M_writer('\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_before_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        theme_config = _import_ns.get('theme_config', context.get('theme_config', UNDEFINED))
        featured = _import_ns.get('featured', context.get('featured', UNDEFINED))
        def before_content():
            return render_before_content(context)
        pagekind = _import_ns.get('pagekind', context.get('pagekind', UNDEFINED))
        is_frontmost_index = _import_ns.get('is_frontmost_index', context.get('is_frontmost_index', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        if 'main_index' in pagekind and is_frontmost_index and featured and (theme_config.get('featured_large') or theme_config.get('featured_small')):
            pass
            if theme_config.get('featured_on_mobile'):
                __M_writer('            <div class="d-block">\n')
            else:
                __M_writer('            <div class="d-none d-md-block">\n')
            if featured and theme_config.get('featured_large'):
                __M_writer('        <div class="jumbotron p-0 text-white rounded bg-dark">\n            <div class="row bootblog4-featured-jumbotron-row">\n                <div class="col-md-6 p-3 p-md-4 pr-0 h-md-250 bootblog4-featured-text">\n                    <h1 class="display-4 font-italic"><a class="text-white" href="')
                __M_writer(str(featured[0].permalink()))
                __M_writer('">')
                __M_writer(str(featured[0].title()))
                __M_writer('</a></h1>\n')
                if featured[0].previewimage:
                    __M_writer('                            <div class="lead my-3 mb-0">')
                    __M_writer(str(featured[0].text(teaser_only=True, strip_html=theme_config.get('featured_strip_html', True))))
                    __M_writer('</div>\n                        </div>\n')
                    if theme_config.get('featured_large_image_on_mobile'):
                        __M_writer('                        <div class="col-md-6 p-0 h-md-250 text-right">\n')
                    else:
                        __M_writer('                        <div class="col-md-6 p-0 h-md-250 text-right d-none d-md-block">\n')
                    __M_writer('                            <img class="bootblog4-featured-large-image" src="')
                    __M_writer(str(featured[0].previewimage))
                    __M_writer('" alt="')
                    __M_writer(str(featured.pop(0).title()))
                    __M_writer('">\n                        </div>\n')
                else:
                    __M_writer('                        <div class="lead my-3 mb-0">')
                    __M_writer(str(featured.pop(0).text(teaser_only=True, strip_html=theme_config.get('featured_strip_html', True))))
                    __M_writer('</div>\n                        </div>\n')
                __M_writer('            </div>\n        </div>\n')
            __M_writer('\n')
            if featured and theme_config.get('featured_small'):
                __M_writer('            <div class="row mb-2">\n')
                if len(featured) == 1:
                    __M_writer('                <div class="col-md-12">\n')
                else:
                    __M_writer('                <div class="col-md-6">\n')
                __M_writer('                    <div class="card flex-md-row mb-4 box-shadow h-md-250">\n                       <div class="card-body d-flex flex-column align-items-start">\n                           <h3 class="mb-0">\n                               <a class="text-dark" href="')
                __M_writer(str(featured[0].permalink()))
                __M_writer('">')
                __M_writer(str(featured[0].title()))
                __M_writer('</a>\n                           </h3>\n')
                if featured[0].previewimage:
                    __M_writer('                               <div class="card-text mb-auto bootblog4-featured-text">')
                    __M_writer(str(featured[0].text(teaser_only=True, strip_html=theme_config.get('featured_strip_html', True))))
                    __M_writer('</div>\n                               </div>\n                               <img class="card-img-right flex-auto d-none d-lg-block" src="')
                    __M_writer(str(featured[0].previewimage))
                    __M_writer('" alt="')
                    __M_writer(str(featured.pop(0).title()))
                    __M_writer('">\n')
                else:
                    __M_writer('                           <div class="card-text mb-auto bootblog4-featured-text">')
                    __M_writer(str(featured.pop(0).text(teaser_only=True, strip_html=theme_config.get('featured_strip_html', True))))
                    __M_writer('</div>\n                           </div>\n')
                __M_writer('                    </div>\n                </div>\n\n')
                if featured:
                    __M_writer('               <div class="col-md-6">\n                    <div class="card flex-md-row mb-4 box-shadow h-md-250">\n                       <div class="card-body d-flex flex-column align-items-start">\n                           <h3 class="mb-0">\n                               <a class="text-dark" href="')
                    __M_writer(str(featured[0].permalink()))
                    __M_writer('">')
                    __M_writer(str(featured[0].title()))
                    __M_writer('</a>\n                           </h3>\n')
                    if featured[0].previewimage:
                        __M_writer('                               <div class="card-text mb-auto bootblog4-featured-text">')
                        __M_writer(str(featured[0].text(teaser_only=True, strip_html=theme_config.get('featured_strip_html', True))))
                        __M_writer('</div>\n                               </div>\n                               <img class="card-img-right flex-auto d-none d-lg-block" src="')
                        __M_writer(str(featured[0].previewimage))
                        __M_writer('" alt="')
                        __M_writer(str(featured.pop(0).title()))
                        __M_writer('">\n')
                    else:
                        __M_writer('                           <div class="card-text mb-auto bootblog4-featured-text">')
                        __M_writer(str(featured.pop(0).text(teaser_only=True, strip_html=theme_config.get('featured_strip_html', True))))
                        __M_writer('</div>\n                           </div>\n')
                    __M_writer('                    </div>\n                </div>\n')
                __M_writer('       </div>\n')
            __M_writer('    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/bootblog4/templates/index.tmpl", "uri": "index.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 4, "32": 5, "35": 6, "41": 0, "84": 2, "85": 3, "86": 4, "87": 5, "88": 6, "89": 7, "94": 15, "99": 73, "104": 150, "110": 9, "123": 9, "124": 10, "125": 10, "126": 11, "127": 12, "128": 12, "129": 12, "130": 14, "131": 14, "132": 14, "138": 17, "169": 17, "174": 20, "175": 21, "176": 22, "177": 22, "178": 22, "179": 24, "180": 25, "181": 25, "182": 25, "183": 27, "184": 28, "185": 29, "186": 29, "187": 29, "188": 31, "189": 31, "190": 31, "191": 31, "192": 34, "194": 35, "195": 36, "196": 36, "197": 36, "198": 36, "199": 36, "200": 38, "201": 39, "202": 39, "203": 39, "204": 39, "205": 39, "206": 40, "207": 41, "208": 41, "209": 41, "210": 43, "211": 45, "212": 45, "213": 46, "214": 46, "215": 46, "216": 46, "217": 46, "218": 46, "219": 47, "220": 48, "221": 48, "222": 48, "223": 49, "224": 49, "225": 49, "226": 49, "227": 49, "228": 49, "229": 51, "230": 53, "231": 54, "232": 54, "233": 54, "234": 56, "235": 58, "236": 59, "237": 60, "238": 60, "239": 62, "240": 63, "241": 64, "242": 64, "243": 67, "244": 69, "245": 70, "246": 70, "247": 71, "248": 71, "249": 72, "250": 72, "256": 18, "266": 18, "267": 19, "268": 19, "274": 75, "287": 75, "288": 76, "290": 77, "291": 78, "292": 79, "293": 80, "294": 82, "295": 83, "296": 86, "297": 86, "298": 86, "299": 86, "300": 87, "301": 88, "302": 88, "303": 88, "304": 90, "305": 91, "306": 92, "307": 93, "308": 95, "309": 95, "310": 95, "311": 95, "312": 95, "313": 97, "314": 98, "315": 98, "316": 98, "317": 101, "318": 104, "319": 105, "320": 106, "321": 107, "322": 108, "323": 109, "324": 110, "325": 112, "326": 115, "327": 115, "328": 115, "329": 115, "330": 117, "331": 118, "332": 118, "333": 118, "334": 120, "335": 120, "336": 120, "337": 120, "338": 121, "339": 122, "340": 122, "341": 122, "342": 125, "343": 128, "344": 129, "345": 133, "346": 133, "347": 133, "348": 133, "349": 135, "350": 136, "351": 136, "352": 136, "353": 138, "354": 138, "355": 138, "356": 138, "357": 139, "358": 140, "359": 140, "360": 140, "361": 143, "362": 146, "363": 148, "369": 363}}
__M_END_METADATA
"""
