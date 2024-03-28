<!--
.. title: Another Appreciation for RSS
.. slug: happy-bday-RSS
.. date: 2024-03-25 03:20:00 UTC-04:00
.. tags: tech, RSS
.. category: technology
.. previewimage:
.. description: Happy birthday RSS!
.. type: text
-->


Got a bit of a quick one for you today.

On March 15th, 1999, RSS was initially released to the world on the Netscape.com portal.


Previously, I wrote about RSS as a part of an experiment where I tried to find one cool thing weekly.
I failed at that experiment, but I think it was a good experiment. It's a shame it had to be on substack first.

So now, I revive that post somewhat in an in-depth appreciation for RSS.

Happy birthday.

<!-- TEASER_END -->

### Vaguely Technical: RSS format
 RSS uses XML formatting to describe a feed and its items. Whilst XML causes some developers to get the thousand-yard stare, myself somewhat included, I have used it before with little issue.

 My favorite creation was an RSS feed reading bot for News and Podcasts I used for an XMPP server. It just fit right in and it posts to some MUCs we have setup. We love newsbot in this house.

 To give an example of RSS' XML format, here's an entry from my [infosec.town](https://infosec.town) account:

```xml
<item>
    <title><![CDATA[Build target: _katerina 🏳️‍⚧️ renotes]]></title>
    <link>https://infosec.town/notes/9qi6i8sau4gzl45f</link>
    <guid>https://infosec.town/notes/9qi6i8sau4gzl45f</guid>
    <pubDate>Tue, 05 Mar 2024 16:58:57 GMT</pubDate>
    <content:encoded><![CDATA[ <span class="renote_note without_img"></span><hr>Jerry Bell :verified_paw: :donor: :verified_dragon: :rebelverified:​(@jerry@infosec.exchange) says:                        <br>
    Sites available
    ❌Facebook
    ❌instagram
    ✅Infosec.exchange
    ]]>
    </content:encoded>
</item>
```
This is certainly not the cleanest example, but it's still pretty simple. This describes a repost on my account, with a link, publish date, and encoded content.
If I were using a feed reader like feedly or something, I could see all of my posts in chronological order, including reposts, in one feed. I could do that for other accounts, too!
I could have a mixed feed of webcomics, News, and social media posts in one app. [Feedly](https://feedly.com/), as mentioned prior is a popular option, but I'm pretty attached to using local apps in my terminal and such.
The tags, as far as I'm aware, are generally pretty standard across RSS versions (though things like ATOM have some extra fields added that break compatibility somewhat). This makes making things that use it *incredibly easy* to develop, such as the aforementioned RSS feed reading bot.

### The Social

To appreciate RSS, one must contemplate how often they interact with it.

As an avid podcast listener, I interact with it pretty much daily. Whilst apps like Google Podcasts exist[^1], I tend to veer towards the open-source. For a long time I used gPodder on PC, but for want of synchronization and modernity, I moved over to KDE's Kasts on Desktop and Laptops, and Antennapod for mobile. I sync my subscriptions with a nextcloud instance. It treats me pretty well!

Pretty much all of my podcasts have easily-found RSS feeds, and in the worst scenarios (like podcasts only hosted on Apple podcasts for some reason?) I can use something like [Get RSS Feed](https://getrssfeed.com/).

Why does my podcast behavior matter? Well, it's a form of curation.

I can self-curate pretty much any content I wish so long as it has an RSS feed. News sites, blogs, podcasts. I have control and authority over what I can read. This is *incredibly powerful* for ingesting content.
At one point, even Facebook and Twitter had RSS feeds. Those things are gone now, but many Fediverse platforms support it, and the protocol is primarily chronological, making self-curation easy.

In the modern era, we've become incredibly reliant on algorithmic news feeds to deliver us headlines and content.

I propose that with RSS slowly regaining its appeal, that we cultivate a new era of web syndication. RSS does the job well, is used constantly in various types of places like blogs and podcasts, and is interoperable.

Google Reader might be dead, algorithms might have made decisions for us in the past, but self-curation and interoperability are incredibly powerful. Not to mention, for me, it feels more human.

Thank you, RSS.


[^1]: [Oops! My bad! Add it to the graveyard.](https://arstechnica.com/gadgets/2023/12/google-podcasts-dies-april-2024-youtube-music-migration-tool-goes-live/)
