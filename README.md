# My personal website
Built using [Astro](https://docs.astro.build)

## Commands
| Command                   | Action                                           |
| :------------------------ | :----------------------------------------------- |
| `npm install`             | Installs dependencies                            |
| `npm run dev`             | Starts local dev server at `localhost:4321`      |
| `npm run build`           | Build your production site to `./dist/`          |
| `npm run preview`         | Preview your build locally, before deploying     |
| `npm run astro ...`       | Run CLI commands like `astro add`, `astro check` |
| `npm run astro -- --help` | Get help using the Astro CLI                     |
| `npx astro sync`          |                                                  |
| `git push origin main:deploy` | Deploy                                       |

## Content Notes

### Blog
All blog posts use either the `ShortPost` or `LongPost` layout. Use the short posts for image-oriented content and long posts for long-form content.

#### Frontmatter
| Field     | Parameters  | Required?     | Description   |
| :--       | :--   | :--           | :--           |
| type  | `long` or `short`  |  Y   | Specifies long or short post  |
|  title | string  |  Y |   |
|  description | string   |  Y |   |
|  featuredImage | image path  | Y  | Used for thumbnails and the first photo of long posts |
| images | array of image paths  | N  |  Used for image reel in short posts |
|  pubDate | `YYYY-MM-DD`  |  Y |  Date published |
|  updatedDate | `YYYY-MM-DD`   |   N | Date revised  |
|  featured |  boolean | N  |  Whether to feature post in main gallery. Defaults to false. |
|  tags |  see list of tags | N  |   |

See `src/content/config.ts` for schema definition.

##### List of Tags
- `sewing` 
- `knitting` 
- `crochet` 
- `lace` 
- `bobbin lace` 
- `weaving` 
- `tools` 
- `misc`  

See `src/content/config.ts` for the authoritative list of tags.

### Notebook: Cooking

#### Frontmatter

| Field     | Parameters  | Required?     | Description   |
| :--       | :--   | :--           | :--           |
| title  | string  |  Y   |   |
| description  | string  |  N   |  For individual recipes, shown on thumb cards. |
| grade  | `['E', 'A', 'D', 'B', 'S']`  |  Y  |  Grade completion status of entry |
| images  | array of image paths  |  N   |  For photo reels at the end of individual recipes |
| customFolderOrder  | array of folder names  |  N   |  For folders, to force the displayed order of sub-folders |

#### Recipe Style Conventions

- **General structure:** A list of ingredients followed by directions in paragraph format. The recipe may be followed by a horizontal rule and a bulleted "Notes: " section.
- **For foreign languages:** Titles in different languages may be followed by English in parenthesis if an English name is also common. Titles should always be romanized. Alternate names or scripts may be listed at the beginning of descriptions in parenthesis, separated by commas.
- List each ingredient first by quantity (optional), then by name, followed by a comma and descriptor (optional). Multiple ingredients may be listed in one bullet point, separated by semicolon. Descriptors applying to all ingredients use an em dash. Non-active descriptors can be in parenthesis next to the name of the ingredient. May be followed by a period and then additional comments. Do not end-punctuate.
    - e.g. "1 onion (or shallot), chopped; 3 cloves garlic, minced; 1-inch piece ginger (opt.), grated — all sautéed in olive oil"
    