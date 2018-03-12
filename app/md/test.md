# Markdown!

***This is a TEST markdown page***


## Exernal media

In pure MD we cannot really embed a media, but we can have an image with a link to it. Alternatively we can use a iframe Embed (see next section).

### Youtube

```
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg)](https://www.youtube.com/watch?v=YOUTUBE_VIDEO_ID_HERE)
```

[![Fire](https://img.youtube.com/vi/OD4hRY-eAJ0/0.jpg)](https://www.youtube.com/watch?v=OD4hRY-eAJ0)

### Vimeo

It works the same but you need to retrieve the URL of the thumbnail. You can use [this tool](https://deponewd.github.io/video/) to get the thumbnail, its size is just specified in the URL.
```
[![IMAGE ALT TEXT HERE](VIMEO_VIDEO_THUMBNAIL_HERE)](https://vimeo.com/VIMEO_VIDEO_ID_HERE)
```

[![Water](https://i.vimeocdn.com/video/469651458_480x360.jpg)](https://vimeo.com/90429499)

## iFrame

iFrames just work.

```html
<iframe
	src="https://player.vimeo.com/video/90429499"
	width="640"
	height="360"
	frameborder="0"
	webkitallowfullscreen
	mozallowfullscreen
	allowfullscreen
></iframe>
<p>
	<a href="https://vimeo.com/90429499">Water</a> from <a href="https://vimeo.com/morganmaassen">Morgan Maassen</a> on <a href="https://vimeo.com">Vimeo</a>.
</p>
```
<iframe src="https://player.vimeo.com/video/90429499" width="640" height="360" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
<p><a href="https://vimeo.com/90429499">Water</a> from <a href="https://vimeo.com/morganmaassen">Morgan Maassen</a> on <a href="https://vimeo.com">Vimeo</a>.</p>
