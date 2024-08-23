import { defineConfig } from 'astro/config';
import { remarkDefinitionList, defListHastHandlers } from 'remark-definition-list';

import mdx from "@astrojs/mdx";

// https://astro.build/config
export default defineConfig({
  site: 'https://goldinvo.com',
  integrations: [mdx()],
  markdown: {
    remarkPlugins: [remarkDefinitionList],
    remarkRehype: { handlers: defListHastHandlers },
  },
});