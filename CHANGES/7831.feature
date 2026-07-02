Added an optional ``base_version`` filter to the content list endpoints. When combined with
``repository_version_added`` or ``repository_version_removed``, it returns the net set of content
added or removed between two arbitrary repository versions instead of only the single-step
difference against the filtered version's immediate predecessor.
