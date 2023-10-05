<!--
.. title: Prelude to Synchronization
.. slug: prelude-to-sync
.. date: 2023-10-05 12:00:00 UTC-04:00
.. tags: blog meta, dev, ops, projects
.. category: personal
.. link: https://blog.autumnrain.cc/posts/prelude-to-sync
.. description: "Channel Training: Line: 0, vector_state: 4, enabled: 0..."
.. type: text
-->


Autumn's here, and that means it's time to iterate harder.

Typically, I have avoided posting what I do at all outside of a specific thing due to a perceived lack of interest, but Months are actually considerable periods of time when you're doing a lot of waiting, and a lot has been happening recently. From a blog authorship perspective, I'm more realizing at this stage that I just shouldn't care about constantly posting actual interesting things, since that was the pre-switch format in the first place. I simply do not think I'm cut out for content creation in that way. 

<!-- TEASER_END -->

The monthly format as of current was actually unintentional: I was between jobs and spiraling pretty hard when I was making those posts. Now the situation has evolved. I am working, but I'm also trying to go back to school, I'm still working on a few projects, and I'm still mostly playing catch-up. My mental energy is definitely pretty low almost all of the time. This being said, however, I believe I have reached a stage where I can start posting somewhat more regularly, even if it's not the most interesting thing in the world. I would generally point out how completely uninteresting I think I am, but I will leave that determination up to the reader. 

As a fun thing, a couple weeks ago I installed Gentoo on one of my aging laptops and realized the horror and monotony of compiling the GNOME desktop environment on a [2C4T chip from seven years ago](https://www.intel.com/content/www/us/en/products/sku/95443/intel-core-i57200u-processor-3m-cache-up-to-3-10-ghz/specifications.html). Needless to say, I stopped that after awhile and just went with [Awesome](https://awesomewm.org/), which I had never tried before and I actually enjoy using. I've been customizing and configuring the machine between sleep and shifts, so the total amount of time I've thrown into it is like maybe a weekend. Though the machine was practically functional after the first couple hours post-install, it was still super fidgety due to the lack of front-ends and etc. I elected, additionally, to customize the bootloader despite the fact that I find it more or less unnecessary - I had actually never done it before and it was *somewhat* painless except for one absolutely annoying thing: grub hates most of the fonts I throw at it, and it looks... dire. I am looking for some fonts to throw at it that aren't totally butchered by `grub2-mkfont` but it's frankly been taking more time than I really want to throw at it.

As an aside, I have swapped to [OpenTofu](https://opentofu.org/) for provisioning now that it's available, and I'm pleased that my previous TF files are just drop-in, for now. I look forward to see where it goes from here.

Before the Gentoo laptop, I had another go at installing OpenBSD on a VM because the last time I did, it was quirky and on hardware that was incredibly aged. This was fine, actually,  but it wasn't really usable as a proper client machine at the time. The main thing I learned from it was that the install is easier than I remember and XFCE is actually super easy to customize.

I have some things to do, namely some blog customization stuff (I'm trying to figure out a way to add fields in some areas which isn't super hard, but I want it broken out to a markdown meta header...), I have a laptop I'm eyeing to replace my ever-aging Thinkpad T460 as my main "go box" for school, and I'm still dinking around with the Jabber protocol, albeit slowly. I'm also trying to decide whether or not I should make a new theme for both my website and blog (for parity) since it was about this time last year that I updated it. As such, a follow-up will be forthcoming.

Stay warm out there.
