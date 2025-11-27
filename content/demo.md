Title: Demo Post
Author: Sean Hammond
Date: 2024-09-04
Category: Tech
Summary: This is the demo site for [Sidecar](https://github.com/seanh/sidecar),
    a plain but pretty theme for the [Pelican](https://getpelican.com/) static
    site generator. This post demos a few of the things you can do with Sidecar&hellip;

This is the demo site for [Sidecar](https://github.com/seanh/sidecar),
a plain but pretty theme for the [Pelican](https://getpelican.com/) static
site generator. This post demos a few of the things you can do with Sidecar.

See [Sidecar's README](https://github.com/seanh/sidecar) for more features and
customization settings.

<h2 class="notoc">Tables of contents</h2>

Put `<div class="toc"></div>` anywhere in a post or page and it'll be turned
into a table of contents like this:

<div class="toc"></div>

If you have any headings that you don't want to be in the table of
contents put the CSS class `"notoc"` on them:
`<h2 class="notoc">...</h2>`

## Code blocks with syntax highlighting

See [Syntax highlighting](https://docs.getpelican.com/en/latest/content.html#syntax-highlighting)
in Pelican's docs and see the Pygments site for the available
[language names](https://pygments.org/languages/).

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

## Figures

You can create figures with captions using the standard HTML
[`<figure>`](https://html.spec.whatwg.org/multipage/grouping-content.html#the-figure-element)
and [`<figcaption>`](https://html.spec.whatwg.org/multipage/grouping-content.html#the-figcaption-element)
elements:

<figure>
  <img src="{static}/images/sidecar.jpg" alt="A photo of a motorbike with a sidecar">
  <figcaption>Photo by <a href="https://unsplash.com/@hdsfotografie95?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">hidde schalm</a> on <a href="https://unsplash.com/photos/blue-tricycle-parked-beside-house-38FLdKhz_rM?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
  </figcaption>
</figure>

Embedded videos and audio with standard HTML [`<video>`](https://html.spec.whatwg.org/multipage/media.html#the-video-element)
and [`<audio>`](https://html.spec.whatwg.org/multipage/media.html#the-audio-element)
elements also work.

## Block quotes

> The important thing is not to stop questioning. Curiosity has its own reason
> for existence. One cannot help but be in awe when contemplating the mysteries
> of eternity, of life, of the marvelous structure of reality. It is enough if
> one tries merely to comprehend a little of this mystery every day. Never lose
> a holy curiosity.

— Albert Einstein

## Nested lists

* Vivamus non arcu quis sem aliquam
* Quisque in quam tempor, finibus odio nec
* Aenean lacinia augue vel orci efficitur
* Mauris nec sem dapibus, convallis dolor eu
    1. Ut quis neque ac lectus vestibulum
    2. Fusce congue tortor blandit elit
    3. Suspendisse porttitor justo at massa
        * Vestibulum a turpis non urna
        * nteger non orci a ex aliquam
        * ullam sit amet turpis sit amet
    4. Cras nec nulla tincidunt
* Vivamus ullamcorper orci a leo pretium
* Maecenas volutpat est eget purus placerat

## Definition lists

Lists of terms and their definitions, questions and answers, etc.

<dl>
<dt>Oatcake</dt>
<dd>Thin flat unleavened cake of baked oatmeal.</dd>
<dt>Oatmeal</dt>
<dd>Porridge made of rolled oats.</dd>
</dl>

## Disclosure widgets

You can create collapsible disclosure widgets with the standard HTML
[`<details>`](https://html.spec.whatwg.org/multipage/interactive-elements.html#the-details-element)
and [`<summary>`](https://html.spec.whatwg.org/multipage/interactive-elements.html#the-summary-element) elements:

<details>
  <summary>This is the summary</summary>
  <p>And here are the details:</p>
  <ol>
    <li>Cash on hand: $500.00</li>
    <li>Current invoice: $75.30</li>
    <li>Due date: 5/6/19</li>
  </ol>
</details>

## Lead paragraphs

You can create large-text "lead" paragraphs with `<p class="lead">...</p>`:

<p class="lead">
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam vitae ex eros.
Sed nec lacinia turpis. Donec nec nisi et dolor tincidunt commodo vulputate eu
sem. Interdum et malesuada fames ac ante ipsum primis in faucibus.
</p>

## Note boxes

You can create highlighted note boxes with
<code class="nowrap">&lt;p class="note"&gt;...&lt;/p&gt;</code>
(or <code class="nowrap">&lt;div class="note"&gt;...&lt;/div&gt;</code> for a multi-paragraph note box,
<code class="nowrap">&lt;ol class="note"&gt;...&lt;/ol&g with `<s>` or `<del>`t;</code>,
<code class="nowrap">&lt;ul class="note"&gt;...&lt;/ul&gt;</code>,
<code class="nowrap">&lt;aside class="note"&gt;...&lt;/aside&gt;</code>,
etc).

<p class="note"><b>Note</b>: morbi sed facilisis nunc. Quisque dictum lectus vitae purus lobortis, dapibus malesuada sapien imperdiet. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae.</p>

## Grab bag

Keyboard input with `<kbd>`: <kbd>Ctrl</kbd> + <kbd>F1</kbd>,
<span class="badge">badges</span> with `<span class="badge">`,
<mark>highlights</mark> with `<mark>`,
<s>strike-throughs</s> with `<s>` or `<del>`, etc.

## Oatcake

Sidecar is based on [Oatcake](https://www.seanh.cc/oatcake/),
a typography stylesheet. Most of Sidecar's features come from Oatcake and
there's much more than what's been shown in this post. See
[Oatcake's site](https://www.seanh.cc/oatcake/) for more.
