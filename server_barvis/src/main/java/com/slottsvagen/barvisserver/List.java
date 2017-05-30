package com.slottsvagen.barvisserver;

import lombok.Data;

import javax.persistence.*;
import javax.validation.constraints.NotNull;
import java.util.Collection;

/**
 * Represents a list in the database. Used to keep track of information.
 *
 * @author Fredrik Omstedt
 */
@Data
@Entity
@Table(name = "List")
public class List {
    private @Id @GeneratedValue long listId;
    private @NotNull String name;

    @OneToMany(mappedBy = "list")
    private Collection<ListElement> listElements;

    public List() {

    }
}
