import { defineCollection, z } from 'astro:content';

const blog = defineCollection({
	type: 'content',
	schema: z.object({
		type: z.enum(['long', 'short']),
		title: z.string(),
		description: z.string(),
		featuredImage: z.string(),
		images: z.array(z.string()).optional(),
		// Transform string to Date object
		pubDate: z.coerce.date(),
		updatedDate: z.coerce.date().optional(),
		featured: z.boolean().optional(),
		tags: z.array(z.enum(['tools'])).optional(),
	}),
});

const cooking = defineCollection( {
	type: 'content',
	schema: z.object({
		title: z.string(),
		description: z.string().optional(),
		grade: z.enum(['E', 'A', 'D', 'B', 'S']),
		images: z.array(z.string()).optional(),
		customFolderOrder: z.array(z.string()).optional(),
	}),
});

export const collections = { blog, cooking };
