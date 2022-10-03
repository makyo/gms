# gms

Generate movement scripts for Camera2 in Beat Saber using a simplified format and existing cameras

## Scripts so far

* Slow weave - weaves between five camera angles, 10s per angle, 10s transitions ([example](https://www.youtube.com/watch?v=WCGhZ0fDx5w))
* [Tanger - Aurora](https://beatsaver.com/maps/2707c) - could use some work still ([example](https://www.youtube.com/watch?v=HtkSl8XVH_0))

## Cameras included

* \_modleft/\_modright/\_modcenter - three cameras useful for modmaps, as they're further away, shallower, and wider FOV for pretty maps
* \_normalleft/\_normalright - two cameras useful for more standard maps, closer in to your avatar.

## Input format

The input format is just a YAML file that acts as a simplified version of the Camera2 Movement Scripts, in that it allows you to specify frames where a camera should hold for a certain amount of time and then transition to the next frame. Each frame consists of a `start` and an `end`, as well as a `base`, which is the existing camera in the `Cameras` directory containing the required position.

So, for example, I have the cameras `_modleft`, `_modright`, and `_modcenter` set up in Camera2 for use with modmaps. They're not attached to any scenes and are set at the bottom of all the layers. The [map for Tanger's Aurora](https://beatsaver.com/maps/2707c) by [nasafrasa](https://beatsaver.com/profile/4340055) has walls on either side that would obscure a stationary camera, so I want to have the camera weave between them. I took notes on when those walls occur - their `start` and `end` times - and compiled that into a list to have the camera positioned on the opposite side, basing that position off my existing cameras (if the wall is on the left, use `_modright`'s position; if it's on the right use `_modleft`'s; and if on both sides, use `_modcenter`).

This gets me an [input file](2707c-aurora.yaml) that looks like this:

```yaml
- start: 0
  end: 10
  base: _modright
- start: 29
  end: 30
  base: _modcenter
  transition: Eased
- start: 33
  end: 33.01
  base: _modleft
  transition: Eased
- start: 36
  end: 36.01
  transition: Eased
  base: _modright
- start: 39
  end: 40
  base: _modcenter
  transition: Eased
- start: 43
  end: 44.824
  base: _modleft
  transition: Eased
- start: 46
  end: 46.5
  base: _modright
- start: 47.5
  end: 47.51
  base: _modleft
- start: 49
  end: 51
  base: _modright
. . .
```

Running `gms.py` on this file in your Camera2 directory will output a [movement script](2707c-aurora.json) that you can put in an appropriate file in your `MovementScripts` directory. You'll have to add that movement script to whichever camera you are using [per the wiki](https://github.com/kinsi55/CS_BeatSaber_Camera2/wiki/Movement-Scripts).

This leads to a camera path like [this](https://www.youtube.com/watch?v=HtkSl8XVH_0).

## To do

I'd love to be able to read the `<difficulty>.json` and generate an input file to use as a starting point (since it'd likely need tweaking after the fact), but that's a ways off.
