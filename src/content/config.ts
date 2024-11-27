import { defineCollection, z } from 'astro:content';
import { POST_TAGS } from '@constants';


const blog = defineCollection({
	type: 'content',
	schema: ({image}) => z.object({
		type: z.enum(['long', 'short']),
		title: z.string(),
		description: z.string(),
		featuredImage: image(),
		images: z.array(image()).optional(),
		// Transform string to Date object
		pubDate: z.coerce.date(),
		updatedDate: z.coerce.date().optional(),
		featured: z.boolean().optional(),
		tags: z.array(z.enum(POST_TAGS)).optional(),
	}),
});

const cooking = defineCollection( {
	type: 'content',
	schema: ({image}) => z.object({
		title: z.string(),
		description: z.string().optional(),
		grade: z.enum(['E', 'A', 'D', 'B', 'S']),
		images: z.array(image()).optional(),
		customFolderOrder: z.array(z.string()).optional(),
	}),
});

export const collections = { blog, cooking };
