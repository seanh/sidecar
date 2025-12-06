Title: About
Summary:
    <p>
      <a href="https://github.com/seanh/sidecar">Sidecar</a> is a plain but
      pretty theme for the <a href="https://getpelican.com/">Pelican</a> static
      site generator that works great on both mobile and desktop. It's based
      on <a href="https://www.seanh.cc/oatcake/">Oatcake</a>, my universal
      typography stylesheet.
    </p>
    <p>
      This <i>About</i> page is an example of what a static page looks like with
      Sidecar. For installation instructions and configuration settings see the
      <a href="https://github.com/seanh/sidecar">README on GitHub</a>. The rest
      of this page will demo some of Sidecar's features.
    </p>
Stylesheet:
    .example {
      margin-left: var(--ok-line-height);
      margin-right: var(--ok-line-height);
    }
Modified: 2015-12-05

(P.S. Sidecar's page layout is also inspired by the <a
href="https://klise.vercel.app/">Klisé</a> theme for Jekyll, but it's not an
attempt at a clone: I'm aware of the differences!)

## Tables of contents

Sidecar uses <a href="https://tscanlin.github.io/tocbot/">Tocbot</a> to
support adding tables of contents to pages and articles.
Put `<div class="toc"></div>` anywhere in an article or page and it'll be turned
into a table of contents like this:

<div class="toc"></div>

If you want to omit a heading from the table of contents, add the CSS class
`notoc` to it:

```html
<h2 class="notoc">My Heading</h2>
```

### Anchor links

The table of contents depends on all the page's headings having `id` attributes
so that they have anchor links.
Sidecar uses <a href="https://www.bryanbraun.com/anchorjs/">AnchorJS</a> to add
`id`'s to all your headings automatically, with the `id` values being generated
from the heading contents.

If you want to control a heading's `id` value yourself (for example so it
doesn't change if you re-word the heading), add an `id` attribute manually
as normal and AnchorJS will use it:

```html
<h2 id="my-heading">My Heading</h2>
```

If you _don't_ want a heading to have an anchor link, add the CSS class
`noanchor` (this will also remove the heading from the table of contents):

```html
<h2 class="noanchor">My Heading</h2>
```


## Pages

Sidecar supports all of the different types of pages that Pelican offers:

* Static pages, like this one.
* Articles (blog posts).
  Here's a [dummy text example article]({filename}/sunt_excepturi_eius_nihil_ea_dignissimos_dolores.md)
  that shows off some of the HTML elements you can use.
* The <a href="../">index page</a>: a paginated list of recent articles.
* The <a href="../archives/">archives page</a>: all articles on one page.
* The <a href="../tags/">tags page</a>: a list of all tags, each tag linked to a page listing all posts with that tag.
* The <a href="../categories/">categories page</a>: a list of all categories, each category linked to a page listing all posts in that category.
* The <a href="../authors/">authors page</a>: a list of all authors, each author linked to a page listing all posts by that author.
* "Period archive" pages: pages listing all articles for a given year, month or day.
   For example:
  <a href="../2024/">all articles from 2024</a>,
  <a href="../2024/09/">all articles from September, 2024</a>, or
  <a href="../2024/09/22/">all articles from 22nd September, 2024</a>.

## Summaries

The large-text paragraphs at the top of this page are the page's <i>summary</i>.
You create a summary by adding a `Summary` to your article or page's metadata, like this:

<pre><code>Title: Example Post Title
<mark>Summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin a malesuada orci.</mark>

Nullam at massa eros. Nullam ultricies suscipit volutpat.
Maecenas at elit quis sem semper rutrum eu condimentum lorem&hellip;</code></pre>

You can also use <code>Subtitle: &hellip;</code> or <code>Subheading
&hellip;</code> as aliases for `Summary`. The difference is that if you use
`Summary` Pelican will also use the provided summary in its RSS and Atom feeds
(overriding the default summary that Pelican generates from your article's
body). Whereas if you use `Subtitle` or `Subheading` this will not replace the
article summary in RSS and Atom feeds.

You can also add also add subheadings to `<h2>` or `<h3>` headings within
article or page bodies by wrapping the `<h2>` or `<h3>` in an `<hgroup>`
along with the subheading in one or more `<p>`'s, as
[shown in Oatcake's docs](https://www.seanh.cc/oatcake/#hgroup).

Markdown works in `Summary` by default.
To get Markdown to work in `Subtitle` or `Subheading` add them
to the `FORMATTED_FIELDS` setting in your Pelican config:

```python
# pelicanconf.py

FORMATTED_FIELDS = ["summary", "subheading", "subtitle"]
```

Python-Markdown doesn't allow blank lines within the metadata section at the top
of the file, so to create a multi-paragraph summary you need to use `<p>`'s:

```
Title: About
Summary:
    <p>
      Sidecar is a plain but pretty theme for the Pelican static site generator
      that works great on both mobile and desktop.
    </p>
    <p markdown="1">
      This *About* page is an example of what a static page looks like
      with Sidecar.
    </p>
```

(The `markdown="1"` is needed to enable Markdown syntax within a `<p>`.)

## Custom fonts, colors and CSS

Oatcake provides several variables that you can use to customize its fonts and
colors, and you can add your own CSS to further customize the element styles.
See [Oatcake's site](https://www.seanh.cc/oatcake/) for documentation of all the
variables and examples of custom element styles.
Both Oatcake and Sidecar use [CSS layers](https://developer.mozilla.org/en-US/docs/Web/CSS/@layer)
so your rules will take precedence regardless of specificity.

There are three ways to add custom CSS:

1. You can add a CSS file to your site's [static content](https://docs.getpelican.com/en/latest/content.html#static-content)
   and use the [`STYLESHEET_URL`](https://github.com/seanh/sidecar?tab=readme-ov-file#stylesheet_url)
   setting to inject the stylesheet into your site.

2. You can add some CSS in a `STYLESHEET` setting in your Pelican config file:

        #!python
        # pelicanconf.py

        STYLESHEET = """
            :root {
              --ok-color-bg: #ff851b;
              --ok-color-fg: #85144b;
            }
        """

3. You can add a per-page or per-article stylesheet by adding a `Stylesheet`
   line to your page or article's metadata. This allows you to style different
   pages and articles differently:

        Title: A Page or Article with a Custom Stylesheet
        Stylesheet:
            :root {
              --ok-color-bg: #ff851b;
              --ok-color-fg: #85144b;
            }

        Lorem ipsum dolor sit amet, consectetur adipiscing elit...

## Syntax-highlighted code blocks

## Article and page modification dates

If you add a `Modified` date to an article's metadata it'll be shown in the
article's tagline as its "Last updated" date (TODO: link to example).

By default static pages don't show any created or updated date, but if you add
a `Modified` date to a static page's metadata it'll be shown at the bottom of
the page as "Last updated".

Here's how to add a `Modified` date to a Markdown article or page's metadata:

```
Title: About
Modified: 2015-12-05
```
