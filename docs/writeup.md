## Table of Contents  
* [Phenomena specified by the LinGO Grammar Matrix customization system](#choice)  
* [Phenomena specified by .tdl files](#tdl) 
* [Parse results](#parse)   
* [Limitations](#limitations)
* [Suggestions](#suggestions)


## Phenomena specified by the LinGO Grammar Matrix customization system <a name="choice"/>
### Word Order
The basic word order in Mandarin Chinese is subject-verb-object (SVO), with determiners and auxiliary verbs precede nouns and complements respectively. These phenomena are specified in the `Word Order` section of the customization system.

### Number, Person, Gender

### Case



## Phenomena specified by .tdl files <a name="tdl"/>
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


### True negative
```
delphin select 'i-id i-input where i-wf = 0 and readings = 0' trees/testsuite.01/
```
| No. | Sentence                       | Phenomena               | Remarks |
|-----|--------------------------------|-------------------------|---------|
| 1.  | 一只 狗 一只 猫 追             | Word order              ||
| 2.  | 一只 猫 那只 狗 追             | Word order              ||
| 3.  | 追 那只 狗 一只 猫             | Word order              ||
| 4.  | 追 一只 猫 那只 狗             | Word order              ||
| 5.  | 他 在 唱歌 她                  | Word order              ||
| 6.  | 他 唱歌 要                     | Word order              ||
| 7.  | 他 唱歌 应该 会                | Word order              ||
| 8.  | 他 应该 唱歌 会                | Word order              ||
| 9.  | 他 会 唱歌 应该                | Word order              ||
| 10. | 他 给 了 那个 我 一只 猫       | Pronouns                ||
| 11. | 猫 那只 在 唱歌                | Determiners             ||
| 12. | 猫 在 那只 唱歌                | Determiners             ||
| 13. | 猫 在 唱歌 那只                | Determiners             ||
| 14. | 那个 小明 在 唱歌              | Determiners             ||
| 15. | 他 给 我 了 一只 猫            | Tense Aspect Mood       ||
| 16. | 他 给 我 过 一只 猫            | Tense Aspect Mood       ||
| 17. | 在 唱歌 小明                   | Tense Aspect Mood       ||
| 18. | 他 要 不 唱歌                  | Negation                ||
| 19. | 他 有 没 猫                    | Negation                ||
| 20. | 狗 追                          | Argument Optionality    ||
| 21. | 猫 那只                        | Cognitive Status        ||
| 22. | 猫 一只                        | Cognitive Status        ||
| 23. | 他 会 吗 唱歌                  | Matrix yes-no questions ||
| 24. | 他 吗 会 唱歌                  | Matrix yes-no questions ||
| 25. | 吗 他 会 唱歌                  | Matrix yes-no questions ||
| 26. | 我 小明 他 追 一只 猫          | Coordination            ||
| 27. | 和 我 小明 和 他 追 一只 猫    | Coordination            ||
| 28. | 和 我 和 小明 和 他 追 一只 猫 | Coordination            ||
| 29. | 要 一只 猫 可爱 的             | Adjectives              ||
| 30. | 她 地 高兴 唱歌                | Adverbs                 ||
| 31. | 她 觉得 他 是否 不 会 唱歌     | Embedded declaratives   ||
| 32. | 她 问 他 会 唱歌               | Embedded questions      ||
| 33. | 那只 猫 可爱                   | Non-Verbal Predicates   ||
| 34. | 她 要 一只 猫 白               | Adjectives              ||
| 35. | 她 知道 大概                   | Adjectives              ||

### False positive
```
delphin select 'i-id i-input where i-wf = 0 and readings > 0' trees/testsuite.01/
```
No false positive

### False negative
```
delphin select 'i-id i-input where i-wf = 1 and readings = 0' trees/testsuite.01/
```
| No. | Sentence                 | Phenomena            | Remarks |
|-----|--------------------------|----------------------|---------|
| 1.  | 他 给 了 她              | Word order           |         |
| 2.  | 他 给 了 她 一只 猫      | Word order           |         |
| 3.  | 他 应该 会 唱歌          | Word order           |         |
| 4.  | 我 给 了 他 一只 猫      | Pronouns             |         |
| 5.  | 他 给 了 我 一只 猫      | Pronouns             |         |
| 6.  | 他 给 了 那个 人 一只 猫 | Pronouns             |         |
| 7.  | 他 给 了 我 一只 猫      | Tense Aspect Mood    |         |
| 8.  | 他 给 过 我 一只 猫      | Tense Aspect Mood    |         |
| 9.  | 追                       | Argument optionality |         |
| 10. | 这只 猫                  | Cognitive status     |         |
| 11. | 那只 猫                  | Cognitive status     |         |
| 12. | 一只 猫                  | Cognitive status     |         |
| 13. | 她 要 一只 可爱 的 猫    | Adjectives           |         |
| 14. | 她 高兴 地 唱歌          | Adverbs              |         |


## Limitations <a name="limitations"/>

## Suggestions <a name="suggestions"/>
