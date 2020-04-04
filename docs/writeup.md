## Table of Contents  
* [Phenomena specified by the LinGO Grammar Matrix customization system](#choice)  
* [Phenomena specified by modifying .tdl files](#tdl) 
* [Parse results](#parse)   
* [Limitations](#limitations)
* [Suggestions](#suggestions)


## Phenomena specified by the LinGO Grammar Matrix customization system <a name="choice"/>
### Word Order
The basic word order in Mandarin Chinese is subject-verb-object (SVO), with determiners and auxiliary verbs precede nouns and complements respectively. These phenomena are specified in the `Word Order` section of the customization system.

### Number, Person, Gender
Not specified.

### Case
Not specified.

### Adnominal Possession
Not specified.

### Direct-inverse
Not specified.

### Tense, Aspect and Mood
Verb tenses are not expressed in Mandarin Chinese. Instead several particles are used to express verbal aspect, as given below:
* Perfective aspect "了" (e.g. "他给了她。")
* Imperfective aspect "在" (e.g. "他在唱歌。")
* Experiential aspect "过" (e.g. "他给过她。")

### Evidentials
Not specified.

### Other Features
Although Mandarin Chinese does not distinguish between finite and non-finite verb form, the `Add finite/non-finite FORM feature distinction.` option is still selected as it is a mandatory requirement when presence of auxiliary verbs were specified in the `Word Order` section.

### Sentential Negation
Negation construction in Mandarin Chinese is specified as a `simple` morphosyntactic exponence, in which a negative auxiliary verb "不" is introduced.

### Coordination
Two coordination strategies for the Mandarin Chinese Grammar is specified:
* Monosyndeton ("我 你 和 她")
* Polysyndeton ("我 和 你 和 她")

### Matrix Yes/No Questions
A question in the Mandarin Chinese Grammar is formed by introducing a sentence final particle "吗".

### Information Structure
Not specified.

### Argument Optionality
In Mandarin Chinese, subject dropping can occur with any verb in any context (e.g. "狗追猫。" and "追猫！" are both sensible sentences) while object dropping can only occur with certain lexical entries (e.g. dropping "猫" in "他有猫。" is ok but not "猫" in "狗追猫。").

### Nominalized Clauses
Not specified.

### Clausal Complements
Two types of clausal complements are specified in the Mandarin Chinese Grammar:
* Clausal complements appearing in the same position as regular noun complements without a complementizer (e.g. "她觉得他会唱歌。" with "他会唱歌" as a clausal complement of "觉得").
* Clausal complements appearing in the same position as regular noun complements with a complementizer "是否" (e.g. "她问他是否会唱歌。" with "会唱歌" as a clausal complement of "问").

### Clausal Modifiers
Not specified.

### Morphology
Not applicable.


## Phenomena specified by modifying .tdl files <a name="tdl"/>
### Complement of Auxiliary Verb

### Demonstratives (Determinative Nouns)

### Embedded Clauses



## Parse results <a name="parse"/>
### True Positive
```
delphin select 'i-id i-input where i-wf = 1 and readings > 0' trees/testsuite.01/
```

| No. | Sentence                    | Phenomena                         |
|-----|-----------------------------|-----------------------------------|
| 1.  | 那只 狗 追 一只 猫          | Word order                        |
| 2.  | 一只 猫 追 一只 狗          | Word order                        |
| 3.  | 他 在 唱歌                  | Word order                        |
| 4.  | 他 要 唱歌                  | Word order                        |
| 5.  | 我 会                       | Pronouns                          |
| 6.  | 那里 有 一只 猫             | Case                              |
| 7.  | 那里 有 猫                  | Case                              |
| 8.  | 那里 有                     | Case                              |
| 9.  | 那只 猫 在 唱歌             | Determiners                       |
| 10. | 猫 在 唱歌                  | Determiners                       |
| 11. | 小明 在 唱歌                | Determiners, Tense Aspect Mood    |
| 12. | 他 不 要 唱歌               | Negation                          |
| 13. | 他 没 有 猫                 | Negation                          |
| 14. | 他 有 猫                    | Argument optionality              |
| 15. | 他 有                       | Argument optionality              |
| 16. | 追 猫                       | Argument optionality              |
| 17. | 他 会 唱歌 吗               | Matrix yes-no questions           |
| 18. | 他 不 会 唱歌 吗            | Matrix yes-no questions, negation |
| 19. | 我 和 他 追 一只 猫         | Coordination                      |
| 20. | 我 小明 和 他 追 一只 猫    | Coordination                      |
| 21. | 我 和 小明 和 他 追 一只 猫 | Coordination                      |
| 22. | 她 觉得 他 不 会 唱歌       | Embedded declaratives             |
| 23. | 那只 猫 很 可爱             | Non-Verbal Predicates             |
| 24. | 她 要 一只 白 猫            | Adjectives                        |
| 25. | 她 大概 知道                | Adverbs                           |
| 26. | 她 问 他 是否 会 唱歌       | Embedded questions                |


### True Negative
```
delphin select 'i-id i-input where i-wf = 0 and readings = 0' trees/testsuite.01/
```
| No. | Sentence                       | Phenomena               |    Remarks      |
|-----|--------------------------------|-------------------------|-----------------|
| 1.  | 一只 狗 一只 猫 追             | Word order                 | SOV word order |
| 2.  | 一只 猫 那只 狗 追             | Word order                 | OSV word order |
| 3.  | 追 那只 狗 一只 猫             | Word order                 | VSO word order |
| 4.  | 追 一只 猫 那只 狗             | Word order                 | VOS word order |
| 5.  | 他 在 唱歌 她                  | Word order                | Object in intransitive verb |
| 6.  | 他 唱歌 要                     | Word order                | Auxiliary verb after verb  |
| 7.  | 他 唱歌 应该 会                | Word order                 | Auxiliary verb after verb |
| 8.  | 他 应该 唱歌 会                | Word order                 | Auxiliary verb after verb |
| 9.  | 他 会 唱歌 应该                | Word order                 | Auxiliary verb after verb |
| 10. | 他 给 了 那个 我 一只 猫       | Pronouns                    | Determiner before pronoun |
| 11. | 猫 那只 在 唱歌                | Determiners                | Determiner after noun |
| 12. | 猫 在 那只 唱歌                | Determiners                | Determiner after noun |
| 13. | 猫 在 唱歌 那只                | Determiners                | Determiner after noun |
| 14. | 那个 小明 在 唱歌              | Determiners                | Determiner before proper noun |
| 15. | 他 给 我 了 一只 猫            | Tense Aspect Mood          | Perfective aspect after pronoun |
| 16. | 他 给 我 过 一只 猫            | Tense Aspect Mood          | Experiential aspect after pronoun |
| 17. | 在 唱歌 小明                   | Tense Aspect Mood         | Subject after imperfective aspect |
| 18. | 他 要 不 唱歌                  | Negation                  | Negative auxiliary verb after verb |
| 19. | 他 有 没 猫                    | Negation                  | Negative auxiliary verb after verb |
| 20. | 狗 追                          | Argument Optionality     | Invalid object dropping |
| 21. | 猫 那只                        | Cognitive Status         | Demonstrative after noun |
| 22. | 猫 一只                        | Cognitive Status         | Demonstrative after noun |
| 23. | 他 会 吗 唱歌                  | Matrix yes-no questions   | Sentence final particle before words |
| 24. | 他 吗 会 唱歌                  | Matrix yes-no questions   | Sentence final particle before words |
| 25. | 吗 他 会 唱歌                  | Matrix yes-no questions   | Sentence final particle before words |
| 26. | 我 小明 他 追 一只 猫          | Coordination               | Missing coordinator |
| 27. | 和 我 小明 和 他 追 一只 猫    | Coordination                | Sentence initial coordinator |
| 28. | 和 我 和 小明 和 他 追 一只 猫 | Coordination                | Sentence initial coordinator |
| 29. | 要 一只 猫 可爱 的             | Adjectives                 | Adjective after noun |
| 30. | 她 地 高兴 唱歌                | Adverbs                    | Adverb before adjective |
| 31. | 她 觉得 他 是否 不 会 唱歌     | Embedded declaratives       | Invalid complementizer |
| 32. | 她 问 他 会 唱歌               | Embedded questions         | Missing complementizer or sentence final particle |
| 33. | 那只 猫 可爱                   | Non-Verbal Predicates      | Missing modifier |
| 34. | 她 要 一只 猫 白               | Adjectives                 | Adjective after noun |
| 35. | 她 知道 大概                   | Adjectives                 | Adverb after verb |

### False Positive
```
delphin select 'i-id i-input where i-wf = 0 and readings > 0' trees/testsuite.01/
```
No false positive.

### False Negative
```
delphin select 'i-id i-input where i-wf = 1 and readings = 0' trees/testsuite.01/
```
| No. | Sentence                 | Phenomena            | Remarks |
|-----|--------------------------|----------------------|---------|
| 1.  | 他 给 了 她              | Word order           | Perfective aspect |
| 2.  | 他 给 了 她 一只 猫      | Word order           | Perfective aspect |
| 3.  | 他 应该 会 唱歌          | Word order           | Double auxiliary verbs |
| 4.  | 我 给 了 他 一只 猫      | Pronouns             | Perfective aspect |
| 5.  | 他 给 了 我 一只 猫      | Pronouns             | Perfective aspect  |
| 6.  | 他 给 了 那个 人 一只 猫 | Pronouns             | Perfective aspect |
| 7.  | 他 给 了 我 一只 猫      | Tense Aspect Mood    | Perfective aspect |
| 8.  | 他 给 过 我 一只 猫      | Tense Aspect Mood    | Experiential aspect |
| 9.  | 追                       | Argument optionality | Fragment |
| 10. | 这只 猫                  | Cognitive status     | Fragment |
| 11. | 那只 猫                  | Cognitive status     | Fragment |
| 12. | 一只 猫                  | Cognitive status     | Fragment |
| 13. | 她 要 一只 可爱 的 猫    | Adjectives           | Relative marker |
| 14. | 她 高兴 地 唱歌          | Adverbs              | Adverb of manner |


## Limitations <a name="limitations"/>

## Suggestions <a name="suggestions"/>
