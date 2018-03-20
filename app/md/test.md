# Markdown!

***This is a TEST markdown page***

## External media

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

iFrames just work here.

```
<iframe
	src="https://player.vimeo.com/video/90429499"
	width="640"
	height="360"
	frameborder="0"
	webkitallowfullscreen
	mozallowfullscreen
	allowfullscreen
></iframe>
```

<iframe src="https://player.vimeo.com/video/90429499" width="640" height="360" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>

## Sigma

Sigma cannot be easily embedded, but iFrames can be a solution. Here is for instance an iFrame for a ManyLines. It requires to host minimal sigma pages in this repository.

<iframe 
	src="http://tools.medialab.sciences-po.fr/manylines/embed#/narrative/290135dd-49a6-4a8e-a730-1e7c8c9c7bb2"
	width="800"
	height="480"
	webkitallowfullscreen
	mozallowfullscreen
	allowfullscreen
></iframe>

## Advanced styling

It's possible to use **<span style="color: #AB0000">colors</span> <span style="color: #A000A0">of</span> <span style="color: #6B00A2">any</span> <span style="color: #0000A0">kind</span>** or other advanced styling by using HTML markup.

## Angular directives

You can include Angular directives.

```
<md-button class="md-accent md-raised" ng-href="#!/"><md-icon>home</md-icon> Take me home!</md-button>
```

<md-button class="md-accent md-raised" ng-href="#!/"><md-icon>home</md-icon> Take me home!</md-button>

## Datasets

Angular directives include the custom "dataset-info" directive.

```
Look at this <span info-dataset="corpus-candidats-linkfluence">dataset</span>!
```
Look at this <span info-dataset="corpus-candidats-linkfluence">dataset</span>!
