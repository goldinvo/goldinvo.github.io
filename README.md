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

See recipes graded 'E' for style conventions

#### Frontmatter

| Field     | Parameters  | Required?     | Description   |
| :--       | :--   | :--           | :--           |
| title  | string  |  Y   |   |
| description  | string  |  N   |  For individual recipes, shown on thumb cards. |
| grade  | `['E', 'A', 'D', 'B', 'S']`  |  Y  |  Grade completion status of entry |
| images  | array of image paths  |  N   |  For photo reels at the end of individual recipes |
| customFolderOrder  | array of folder names  |  N   |  For folders, to force the displayed order of sub-folders |


    