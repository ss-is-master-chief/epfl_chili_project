# Large Scale Instructional Design Analysis

* Every learning sequence is stored in their zipped formats
* `tool.xml` per Activity, describes the inner workings of that Activity
* `learning_design.xml` is the main XML script which refer to the `tool.xml` scripts on the basis of `<ActivityID>` values

* `<transitions>` : Contains flow information per connection between activities
```
<transitions>
  <org.lamsfoundation.lams.learningdesign.dto.TransitionDTO>
    <transitionID>891</transitionID>
    <transitionUIID>9</transitionUIID>
    <toUIID>2</toUIID>
    <fromUIID>1</fromUIID>
    <createDateTime class="sql-timestamp">1970-01-01 11:00:00.0</createDateTime>
    <toActivityID>1349</toActivityID>
    <fromActivityID>1348</fromActivityID>
    <learningDesignID>98</learningDesignID>
  </org.lamsfoundation.lams.learningdesign.dto.TransitionDTO>
</transitions>
```
* `<validDesign>` : Parse script if the value is `true`
* `<createDateTime>` : Contains information on when sequence was created. Use this to parse scripts in chronological order
* `<activityCategoryID>` : ?
* `<activityTypeID>` : ?

# Questions

* Are the scripts aware regarding the category to which they belong to?
* How are the data stored in each activity node in the LAMS graphs, expressed in terms of XML? Where is that code block located in the scripts?
* Will XML parsing as Element Tree be the appropriate way to start off with? 
* Would converting them into UML via XSLT processor make it easier to work with later?
* Which would be better - general XML Parsing and scraping information OR treating the files as a corpus of text?
* How can we convert the XML scripts into Neo4J graphs via the Python Driver?
* What are the XML features which the model should take as input for processing?

# LAMS Activities

<div align="center">
<img src="https://wiki.lamsfoundation.org/download/attachments/5570607/types.png?version=1&modificationDate=1260541901000"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px"
/>
</div>