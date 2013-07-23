NaturalJSDocs is a [Sublime Text 2](http://www.sublimetext.com/) package which makes writing JSDoc easy. Based on [NaturalDocs](http://www.naturaldocs.org).

## Autocomplete Comments

If you start a comment block (e.g. `/*`, `/**`, `/*!`) and press enter, it will complete the block and put your cursor in the middle. Subsequently, pressing enter inside a block will create a new line continuing the comment block.

`/**|` -> `Enter`

Results in

```
/**
 * |
 */
```

The above pipe represents the cursor. Pressing `Enter` again will result in this:

```
/**
 *
 * |
 */
```

If you happened to start a block before a function, it would populate the block with the function information.

```
/** |
function testThis($one, $two) {}
```

Results in:

```
/**
 * description
 *
 * @memberof module:com.company.name.modulename#
 * @param $one - [type/description]
 * @param $two - [type/description]
 * @returns description
 */
function testThis($one, $two) {}
```

**Single-line Comments**

Additionally, if you start a single-line comment (e.g. `//` or `#`), pressing `Enter` will continue the comment block on the next line. You can press `Shift-Enter` to just go to a blank line.


## Decorations

You can add decoration blocks by pressing `Ctrl-Enter`.

Examples in JavaScript:

```javascript
// this is a pretty item |
```

Results in:

```javascript
///////////////////////////
// this is a pretty item //
///////////////////////////

# Commands

* NaturalDocsCommand
* NaturalDocsInsertBlock
* NaturalDocsIndentCommand
* NaturalDocsJoinCommand
* NaturalDocsDecorateCommand

# Settings

## natural_docs_deep_indent

This setting controls whether to align lines inside documentation blocks based on the previous line.

When using `Enter` inside a documentation block, NaturalDocs will try to align the start of the next line either (1) after the parameter dash (space-hyphen-space) or (2) at the first actual start of last line. See examples.

Example:

```javascript
  /**
   * ...
   * Parameters:
   *
   *   one     - this parameter does something |
   *   twoLong - string
   */
```

If the current line that contains ' - ', then pressing `Enter` will insert enough spaces to align the cursor under the description of the previous line. Result:

```javascript
  /**
   * ...
   * Parameters:
   *
   *   one     - this parameter does something
   *             |
   *   twoLong - string
   */
```

Similarly, if the current line does not contain ' - ', then pressing `Enter` will insert enough spaces to start the line under the first non-Whitespace character inside the documentation. Starting at:

```javascript
  /**
   * ...
   * Parameters:
   *
   *   one     - this parameter does something
   *             this is another line |
   *   twoLong - string
   */
```

Results in:

```javascript
  /**
   * ...
   * Parameters:
   *
   *   one     - this parameter does something
   *             this is another line
   *             |
   *   twoLong - string
   */
```

If this setting is enabled, and there are no snippet fields available in the documentation block, you can also use `Tab` to insert as many spaces as necessary to put the cursor below the description of the previous line.

```javascript
  /**
   * ...
   * Parameters:
   *
   *   one   - this parameter does something
   * |
   */
```

Pressing `Tab` results in:

```javascript
  /**
   * ...
   * Parameters:
   *
   *   one   - this parameter does something
   *           |
   */
```

## natural_docs_continue_comments

If this setting is set to `True`, then pressing `Enter` on a line with a double-slash or number-sign comment will place that comment punctuation at the beginning of the next line.

Example:

```javascript
// hello |
```

Translates to

```javascript
// hello
// |
```