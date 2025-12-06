Title: About
Summary:
    <b>Sidecar</b> is a plain but pretty theme for the
    <a href="https://getpelican.com/">Pelican</a> static site
    generator that works great on both mobile and desktop. For
    installation instructions and configuration settings see
    <a href="https://github.com/seanh/sidecar"><b>Sidecar's README on
    GitHub</b></a>. This page shows some of the features you can use when
    writing pages and articles.
Stylesheet:
    .example {
      margin-left: var(--ok-line-height);
      margin-right: var(--ok-line-height);
    }
Modified: 2025-12-06

Sidecar is based on **Oatcake** my universal typography theme.
Oatcake styles a wide variety of HTML elements you can use when writing.
The dummy text articles on this demo site show
[some of Oatcake's elements in action]({filename}/sunt_excepturi_eius_nihil_ea_dignissimos_dolores.md).
See [Oatcake's site](https://www.seanh.cc/oatcake/) for full documentation.

Sidecar's page layout is inspired by the <a
href="https://klise.vercel.app/">Klisé theme</a> for Jekyll.
The avatar image on the demo site front page is from [Judy Beth Morris on Unsplash](https://unsplash.com/photos/a-small-dog-wearing-goggles-and-a-vest-D5bZ2wzgUkA):

<img width="1920" height="1440" style="height: auto;" src="{static}/images/dog.jpg" alt="A small dog wearing goggles and a vest." title="A small dog wearing goggles and a vest.">

## Tables of contents

Sidecar uses <a href="https://tscanlin.github.io/tocbot/">Tocbot</a> to
support adding tables of contents to pages and articles.
Put `<div class="toc"></div>` anywhere in an article or page and it'll be turned
into a table of contents like this:

<div class="toc"></div>

<details markdown="1">
  <summary>Omitting headings from tables of contents</summary>
If you want to omit a heading from the table of contents, add the CSS class
`notoc` to it:

```html
<h2 class="notoc">My Heading</h2>
```
</details>

<details markdown="1">
  <summary>Heading anchor links</summary>

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
</details>

## Summaries

The large-text paragraph at the top of this page is the page's <i>summary</i>.
You create a summary by adding a `Summary` to your article or page's metadata, like this:

<pre><code>Title: Example Post Title
<mark>Summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin a malesuada orci.</mark>

Nullam at massa eros. Nullam ultricies suscipit volutpat.
Maecenas at elit quis sem semper rutrum eu condimentum lorem&hellip;</code></pre>

<details markdown="1">
  <summary><b>Details:</b> summaries</summary>

You can also use <code>Subtitle: &hellip;</code> or <code>Subheading:
&hellip;</code> instead of `Summary`. The difference is that if you use
`Summary` Pelican will also use the provided summary in its RSS and Atom feeds
(overriding the default summary that Pelican generates from your article's
body). Whereas if you use `Subtitle` or `Subheading` this will not replace the
article summary in RSS and Atom feeds.

You can also add subheadings to `<h2>` or `<h3>` headings within article
or page bodies by wrapping the `<h2>` or `<h3>` in an `<hgroup>` along
with the subheading in one or more `<p>`'s, as [shown in Oatcake's
docs](https://www.seanh.cc/oatcake/#hgroup).

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
</details>

## Per-page custom styles

You can add site-wide custom CSS to Sidecar using the 
[`STYLESHEET_URL`](https://github.com/seanh/sidecar?tab=readme-ov-file#stylesheet_url)
and
[`STYLESHEET`](https://github.com/seanh/sidecar?tab=readme-ov-file#stylesheet)
settings.
To add _per-page_ or _per-article_ CSS add a `Stylesheet` line to a page
or article's metadata, this way you can style different pages and articles
differently from each other:

<pre><code>Title: A Page or Article with a Custom Stylesheet
<mark>Stylesheet:
    :root {
      --ok-color-bg: #ff851b;
      --ok-color-fg: #85144b;
    }</mark>

Lorem ipsum dolor sit amet, consectetur adipiscing elit&hellip;</code></pre>

## Syntax-highlighted code blocks

See [Syntax highlighting](https://docs.getpelican.com/en/latest/content.html#syntax-highlighting)
in Pelican's docs and see the Pygments site for the available
[language names](https://pygments.org/languages/).
You can choose the syntax highlighting color theme with the
[`SIDECAR_PYGMENTS_THEME`](https://github.com/seanh/sidecar?tab=readme-ov-file#sidecar_pygments_theme)
setting.
Here's a code block with the default theme:

```python
def lorem_ipsum(dolor, sit_amet="default"):
    """
    Consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    """
    magna_aliqua = [i for i in range(10) if i % 2 == 0]
    incididunt_ut_labore = {k: v for k, v in enumerate(magna_aliqua)}

    try:
        for consectetur in incididunt_ut_labore.values():
            if consectetur > 5:
                print("Magna aliqua:", consectetur)
            else:
                print("Ut labore et dolore:", consectetur)
    except Exception as e:
        print("Error:", str(e))
```

## Modification dates

If you add a `Modified` date to an article's metadata it'll be shown in the
article's tagline as its "updated" date (as long as you have `"TIME"` in your
[`SIDECAR_TAGLINE`](https://github.com/seanh/sidecar?tab=readme-ov-file#sidecar_tagline)
setting):

<pre><code>Title: My Article
Date: 2015-11-12
<mark>Modified: 2015-12-05</mark></code></pre>

You can see an example in [this dummy article]({filename}/etiam_elementum_nibh_vel_tincidunt_auctor.md).

_Static pages_ don't show any created or updated date by default, but if you add
a `Modified` date to a static page's metadata it'll be shown at the bottom of
the page as "Last updated", as you can see at the bottom of this page.
