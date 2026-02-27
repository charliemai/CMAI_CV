import { z, defineCollection } from "astro:content";
const blogSchema = z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    updatedDate: z.string().optional(),
    heroImage: z.string().optional(),
    badge: z.string().optional(),
    tags: z.array(z.string()).refine(items => new Set(items).size === items.length, {
        message: 'tags must be unique',
    }).optional(),
});

const storeSchema = z.object({
    title: z.string(),
    description: z.string(),
    custom_link_label: z.string(),
    custom_link: z.string().optional(),
    updatedDate: z.coerce.date(),
    pricing: z.string().optional(),
    oldPricing: z.string().optional(),
    badge: z.string().optional(),
    checkoutUrl: z.string().optional(),
    heroImage: z.string().optional(),
});

// Projects / Tools / Products
// A lightweight schema designed for a "living portfolio".
const projectSchema = z.object({
    title: z.string(),
    description: z.string(),
    // When this project page/content was last meaningfully updated.
    updatedDate: z.coerce.date(),
    // Optional: when the project started or launched.
    pubDate: z.coerce.date().optional(),
    heroImage: z.string().optional(),
    badge: z.string().optional(),
    // External links (optional)
    url: z.string().optional(),
    repo: z.string().optional(),
    demo: z.string().optional(),
    tech: z.array(z.string()).optional(),
    highlights: z.array(z.string()).optional(),
    metrics: z.array(z.string()).optional(),
    tags: z.array(z.string()).refine(items => new Set(items).size === items.length, {
        message: 'tags must be unique',
    }).optional(),
});

export type BlogSchema = z.infer<typeof blogSchema>;
export type StoreSchema = z.infer<typeof storeSchema>;
export type ProjectSchema = z.infer<typeof projectSchema>;

// Learning pages (courses, study notes, demos)
// Intentionally shares most fields with projects so the same UI patterns apply.
const learningSchema = projectSchema.extend({
    provider: z.string().optional(),
    period: z.string().optional(),
    status: z.string().optional(),
});
export type LearningSchema = z.infer<typeof learningSchema>;

const blogCollection = defineCollection({ schema: blogSchema });
const storeCollection = defineCollection({ schema: storeSchema });
const projectsCollection = defineCollection({ schema: projectSchema });
const learningCollection = defineCollection({ schema: learningSchema });

export const collections = {
    'blog': blogCollection,
    'store': storeCollection,
    'projects': projectsCollection,
    'learning': learningCollection,
}