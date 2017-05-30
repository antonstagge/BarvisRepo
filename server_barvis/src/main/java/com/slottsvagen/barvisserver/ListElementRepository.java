package com.slottsvagen.barvisserver;

import org.springframework.data.repository.CrudRepository;

/**
 * Represents a repository for list element entities, which keeps track of the entities in the database.
 *
 * @author Fredrik Omstedt
 */
public interface ListElementRepository extends CrudRepository<ListElement, Long> {
}
