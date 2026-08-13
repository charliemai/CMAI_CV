import { defineConfig } from "astro/config";
import sitemap from "@astrojs/sitemap";

export default defineConfig({
  site: "https://cv.cmai.ai",
  integrations: [
    sitemap({
      filter: (page) => !page.endsWith("/blog/") && !page.endsWith("/services/"),
    }),
  ],
});
