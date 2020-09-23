= Broadcast =

Broadcast is inspired by the [NVIDIA Broadcast App](https://www.nvidia.com/en-us/geforce/broadcasting/broadcast-app/) (creative project names are clearly my strong suit), and takes some practical hints from [Benjamin Elder](https://elder.dev/posts/open-source-virtual-background/), [Fufu Fang](https://github.com/fangfufu/Linux-Fake-Background-Webcam), and [John Emmons](https://github.com/jremmons/pyfakewebcam).

Basically, Nvidia released this awesome app to enable background blur or replacement on a live webcam in realtime, and not tied to whatever video conferencing platform your company happens to use (e.g., Zoom has its own built-in background replacement feature). It's really neat, but it was only released for Windows, and only works for folks with a 20 or 30-series Nvidia GPU. So my immediate goal with this is to enable the same functionality for folks running a GNU/Linux system, and to remove the explicit dependency on having a nice, fancy GPU so that laptop users, for example, can benefit from it as well. Eventually I might target a Windows- or Mac-compatible version (and actually, I don't really know for sure that this **isn't** compatible, it's just totally untested on anything but Ubuntu 20.04), but that's a ways off still.

== Prerequisites ==

  - **OS**: Anything Linux-y. Built and tested on Ubuntu 20.04; YMMV on other distributions.
  - Python 3.x
  - Pip
  - `v4l2` and `v4l2loopback`

== Installation ==

```
git clone git@github.com:wetherc/broadcast.git
cd broadcast
python3 -m pip install .
```

== Usage ==


