---
description: "Curated Sopranos video: scenes, trailers, cast and crew interviews, and video essays on the ending, embedded and annotated."
---

# Video Library

A curated set of embedded clips, trailers, and interviews. Everything here is a public YouTube upload, embedded rather than rehosted; nothing is mirrored by this project.

<div class="grid cards" markdown>

-   :material-movie-play: **[Scenes & Trailers](scenes.md)**

    ---

    The opening credits, the trailers, and the opening scene.

-   :material-microphone: **[Interviews](interviews.md)**

    ---

    Chase on the ending, Gandolfini on the cost of Tony, and the cast on losing him.

-   :material-camera-iris: **[Craft & Video Essays](craft.md)**

    ---

    The best analytical breakdowns of the finale and the show's construction.

</div>

---

## How embeds work here

Videos load through **youtube-nocookie.com**, which suppresses the tracking cookies a standard embed sets before playback, and they load lazily so pages with several clips still open fast.

!!! warning "Links rot"
    This is the most fragile part of the wiki. Uploads get taken down, made private, or region-locked without notice, and clips from a rights-holder as active as HBO are more prone to it than most. Every video here was verified when added; some will break.

    **Found a dead embed?** [Open an issue](https://github.com/joedef/sopranos-wiki/issues) or replace it in a pull request. Preference order: an **official HBO** upload, then a documented press or archival channel, then anything else.

## What we don't embed

- Full episodes, or substantial portions of them
- Re-uploads that strip the original uploader's credit
- Anything behind a paywall the embed can't play

## Adding a video

```html
<div class="video">
  <iframe src="https://www.youtube-nocookie.com/embed/VIDEO_ID"
          title="Short description"
          loading="lazy" allowfullscreen
          allow="accelerometer; clipboard-write; encrypted-media; picture-in-picture; web-share"
          referrerpolicy="strict-origin-when-cross-origin"></iframe>
</div>

**Title.** One or two sentences on what it is and why it's worth watching. — *Channel*
{ .video-caption }
```

Write the caption so the entry still means something **after the video dies**. "Watch this" is worthless the moment the embed goes dark; a caption that says what the clip contains still tells a reader what to look for.
