import rss from "@astrojs/rss";
import { SITE_DESCRIPTION, SITE_TITLE } from "../config";
import { writing } from "../data/site";

export const GET = ({ site }) =>
  rss({
    title: SITE_TITLE,
    description: SITE_DESCRIPTION,
    site: site ?? "https://cv.cmai.ai",
    items: writing.map((post) => ({
      title: post.title,
      pubDate: new Date(post.date + "-01-01"),
      description: post.summary,
      link: "/writing/#" + post.slug,
    })),
  });
